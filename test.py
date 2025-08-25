import React, { useEffect, useMemo, useState } from "react";
import { motion } from "framer-motion";

/**
 * Kitty Birthday Fortune – 생일(date)만 입력하면 운세 표시
 * - Input: 생일 (YYYY-MM-DD)
 * - Output: 오늘의 운세 + 행운의 색 + 행운의 행동 (헬로키티 이미지 지원)
 * - FX: 상시 반짝임, 결과 표시 시 하트 폭죽
 * - 외부 아이콘/라이브러리 불필요 (framer-motion만 사용)
 * - /public/kitty.png 넣으면 실사 이미지 사용, 없으면 SVG 대체
 */

// ----------------------
// Kitty fallback SVG (IP-safe)
// ----------------------
const KittySVG = ({ size = 128 }) => (
  <svg width={size} height={(size * 3) / 4} viewBox="0 0 120 90" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="ribbonGrad" x1="0" y1="0" x2="1" y2="1">
        <stop offset="0%" stopColor="#fda4af" />
        <stop offset="100%" stopColor="#fb7185" />
      </linearGradient>
    </defs>
    <ellipse cx="60" cy="45" rx="45" ry="35" fill="white" stroke="#e11d48" strokeWidth="4"/>
    <circle cx="42" cy="42" r="5" fill="#e11d48"/>
    <circle cx="78" cy="42" r="5" fill="#e11d48"/>
    <ellipse cx="60" cy="54" rx="6" ry="4" fill="#fbbf24" stroke="#e11d48" strokeWidth="2"/>
    <path d="M12 40 H34 M12 50 H34 M86 40 H108 M86 50 H108" stroke="#e11d48" strokeWidth="3" strokeLinecap="round"/>
    <path d="M30 24 L42 4 L52 24" fill="white" stroke="#e11d48" strokeWidth="4"/>
    <path d="M68 24 L78 4 L90 24" fill="white" stroke="#e11d48" strokeWidth="4"/>
    <g transform="translate(85,14)">
      <circle cx="0" cy="0" r="9" fill="#be123c"/>
      <path d="M-26 -10 C -8 -20, -8 20, -26 10 Z" fill="url(#ribbonGrad)"/>
      <path d="M 26 -10 C 8 -20, 8 20, 26 10 Z" fill="url(#ribbonGrad)"/>
    </g>
  </svg>
);

// ----------------------
// Fortune templates (12가지 스타일)
// ----------------------
const TEMPLATES = [
  { text: "활력이 샘솟는 하루! 작은 도전이 큰 행운으로 이어져요.", color: "핑크", action: "새 목표 1가지 적기" },
  { text: "꾸준함의 힘이 보이는 날. 루틴을 지키면 보너스가 와요.", color: "초록", action: "루틴 체크✔" },
  { text: "대화운 상승! 먼저 인사하면 멋진 연결이 생겨요.", color: "노랑", action: "친구에게 안부 톡" },
  { text: "마음이 말랑해지는 날. 가까운 사람과 따뜻한 시간.", color: "하늘색", action: "감사 메시지 보내기" },
  { text: "자신감 MAX! 무대가 있다면 빛날 준비 완료.", color: "금색", action: "당당하게 발표" },
  { text: "디테일이 행운. 정리정돈이 기분까지 바꿔요.", color: "아이보리", action: "책상 10분 정리" },
  { text: "균형감각 굿! 타협점 찾으면 모두가 웃어요.", color: "연분홍", action: "장단점 리스트" },
  { text: "몰입력이 폭발! 집중 타임을 활용해 보세요.", color: "보라", action: "25분 몰입 세션" },
  { text: "모험운 ON! 새로운 시도가 즐거움을 줘요.", color: "파랑", action: "안 하던 것 1개 도전" },
  { text: "끈기가 빛나요. 꾸준한 걸음이 결승선을 부릅니다.", color: "검정", action: "오늘의 우선순위 3" },
  { text: "아이디어 뿜뿜! 떠오르는 생각을 놓치지 마세요.", color: "은색", action: "아이디어 메모" },
  { text: "감성이 충만. 음악과 함께 영감이 와요.", color: "연보라", action: "좋아하는 음악 듣기" },
];

// ----------------------
// Utils
// ----------------------
function getTemplateByBirthday(dateStr) {
  // dateStr: YYYY-MM-DD
  try {
    const [y, m, d] = dateStr.split("-").map((n) => parseInt(n, 10));
    if (!y || !m || !d) return null;
    // 간단한 해시: 월*31 + 일 → 0..11
    const idx = ((m * 31 + d) % TEMPLATES.length + TEMPLATES.length) % TEMPLATES.length;
    return TEMPLATES[idx];
  } catch {
    return null;
  }
}

function useViewport() {
  const [vp, setVp] = useState({ w: 360, h: 640 });
  useEffect(() => {
    const update = () => setVp({ w: window.innerWidth || 360, h: window.innerHeight || 640 });
    update();
    window.addEventListener("resize", update);
    return () => window.removeEventListener("resize", update);
  }, []);
  return vp;
}

function useSparkles(count = 28) {
  const { w, h } = useViewport();
  const [flakes, setFlakes] = useState([]);
  useEffect(() => {
    const arr = Array.from({ length: count }).map((_, i) => ({
      id: i + 1,
      x: Math.random() * (w || 360),
      delay: Math.random() * 5,
      dur: 4 + Math.random() * 6,
      size: 16 + Math.random() * 12,
      char: Math.random() < 0.5 ? "✨" : "★",
      height: h || 640,
    }));
    setFlakes(arr);
  }, [w, h, count]);
  return flakes;
}

function makeHeartsBurst(centerX, centerY, n = 28) {
  const hearts = [];
  for (let i = 0; i < n; i++) {
    const angle = (Math.PI * 2 * i) / n + Math.random() * 0.8;
    const dist = 40 + Math.random() * 120;
    hearts.push({
      id: i + 1,
      x: centerX,
      y: centerY,
      tx: centerX + Math.cos(angle) * dist,
      ty: centerY + Math.sin(angle) * dist,
      dur: 0.9 + Math.random() * 0.6,
      scale: 0.6 + Math.random() * 0.6,
    });
  }
  return hearts;
}

export default function KittyBirthdayFortune() {
  const [birthday, setBirthday] = useState("");
  const [result, setResult] = useState(null);
  const [showBurst, setShowBurst] = useState([]);
  const [imgError, setImgError] = useState(false);
  const { w, h } = useViewport();
  const sparkles = useSparkles(30);

  const today = useMemo(() => {
    const d = new Date();
    const mm = String(d.getMonth() + 1).padStart(2, "0");
    const dd = String(d.getDate()).padStart(2, "0");
    return `${d.getFullYear()}-${mm}-${dd}`;
  }, []);

  const onSeeFortune = () => {
    const tpl = getTemplateByBirthday(birthday);
    if (!tpl) return;
    setResult(tpl);
    // 하트 폭죽 중앙 기준
    const cx = (w || 360) / 2;
    const cy = 240;
    setShowBurst(makeHeartsBurst(cx, cy));
    // 잠시 후 폭죽 숨김
    setTimeout(() => setShowBurst([]), 1500);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-pink-100 to-rose-200 relative overflow-hidden p-6">
      {/* 배경 반짝임 */}
      {sparkles.map((f) => (
        <motion.div
          key={f.id}
          className="absolute pointer-events-none select-none"
          style={{ left: f.x, fontSize: f.size }}
          initial={{ y: -20, opacity: 0 }}
          animate={{ y: f.height + 60, opacity: [0, 1, 0] }}
          transition={{ duration: f.dur, repeat: Infinity, delay: f.delay, ease: "linear" }}
        >
          <span className="text-rose-400">{f.char}</span>
        </motion.div>
      ))}

      {/* 상단 이미지 */}
      <div className="mb-4">
        {imgError ? (
          <div className="text-rose-600">
            <KittySVG size={120} />
          </div>
        ) : (
          <motion.img
            src="/kitty.png"
            alt="Hello Kitty"
            className="w-28 h-28 object-contain drop-shadow-xl"
            initial={{ scale: 0 }}
            animate={{ scale: 1, rotate: [0, 10, -10, 0] }}
            transition={{ duration: 1.1 }}
            onError={() => setImgError(true)}
          />
        )}
      </div>

      <div className="text-center mb-2 text-sm text-rose-600/80">{today}</div>
      <h1 className="text-3xl font-extrabold text-rose-700 tracking-tight mb-3">생일 운세</h1>

      {/* 생일 입력 */}
      <div className="flex items-center gap-2 mb-4">
        <input
          type="date"
          value={birthday}
          onChange={(e) => setBirthday(e.target.value)}
          className="px-3 py-2 rounded-xl border-2 border-rose-300 bg-white/90 text-rose-700 shadow"
        />
        <button
          onClick={onSeeFortune}
          className="px-4 py-2 rounded-xl bg-rose-500 text-white shadow hover:bg-rose-600 active:scale-[0.99]"
        >
          운세 보기
        </button>
      </div>

      {/* 결과 카드 */}
      {result && (
        <motion.div
          className="mt-2 p-4 rounded-2xl bg-white/85 shadow-lg text-center text-rose-700 text-lg max-w-xs space-y-2"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <div>💫 {result.text}</div>
          <div>🎨 행운의 색: <span className="font-semibold">{result.color}</span></div>
          <div>✨ 행운의 행동: <span className="font-semibold">{result.action}</span></div>
        </motion.div>
      )}

      {/* 하트 폭죽 */}
      {showBurst.map((h, i) => (
        <motion.div
          key={h.id}
          className="absolute pointer-events-none select-none"
          initial={{ x: h.x, y: h.y, scale: 0, opacity: 1 }}
          animate={{ x: h.tx, y: h.ty, scale: h.scale, opacity: 0 }}
          transition={{ duration: h.dur, ease: "easeOut" }}
        >
          <span style={{ fontSize: 22 }} className="drop-shadow">💖</span>
        </motion.div>
      ))}
    </div>
  );
}
