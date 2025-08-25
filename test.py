import React, { useState } from "react";
import { motion } from "framer-motion";
import { Sparkles, Stars, RefreshCw } from "lucide-react";

// 별자리 목록 + 운세 메시지 + 행운 요소
const fortunes = {
  양자리: {
    text: "오늘은 에너지가 넘치고 도전이 행운을 가져와요!",
    color: "빨강",
    action: "새로운 계획을 시작하기",
  },
  황소자리: {
    text: "꾸준함이 성과로 이어지는 하루예요.",
    color: "초록",
    action: "자신의 속도로 꾸준히 나아가기",
  },
  쌍둥이자리: {
    text: "새로운 인연과 즐거운 대화가 기다려요.",
    color: "노랑",
    action: "친구에게 먼저 연락하기",
  },
  게자리: {
    text: "가족이나 가까운 사람에게 위로를 받아요.",
    color: "하늘색",
    action: "따뜻한 메시지 보내기",
  },
  사자자리: {
    text: "당당함이 매력이 되는 날이에요.",
    color: "금색",
    action: "자신감 있게 발표하기",
  },
  처녀자리: {
    text: "세심함이 좋은 결과를 만들어요.",
    color: "하얀색",
    action: "작은 일도 꼼꼼히 챙기기",
  },
  천칭자리: {
    text: "균형 잡힌 선택이 행운을 가져와요.",
    color: "핑크",
    action: "주변 의견을 들어보기",
  },
  전갈자리: {
    text: "몰입이 큰 성취로 이어질 거예요.",
    color: "보라",
    action: "한 가지에 집중하기",
  },
  사수자리: {
    text: "새로운 모험이 당신을 반기고 있어요.",
    color: "파랑",
    action: "평소 안 하던 활동 도전하기",
  },
  염소자리: {
    text: "끈기가 빛을 발하는 하루예요.",
    color: "검정",
    action: "목표를 메모해두기",
  },
  물병자리: {
    text: "창의적인 아이디어가 떠오를 거예요.",
    color: "은색",
    action: "아이디어를 기록하기",
  },
  물고기자리: {
    text: "감성이 풍부해져 좋은 영감을 받아요.",
    color: "연보라",
    action: "음악 들으며 산책하기",
  },
};

export default function KittyZodiacFortune() {
  const [sign, setSign] = useState("");
  const [fortune, setFortune] = useState(null);

  const handlePick = () => {
    if (!sign) return;
    setFortune(fortunes[sign]);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-b from-pink-100 to-rose-200 relative overflow-hidden">
      {/* 배경 특수효과 */}
      {[...Array(30)].map((_, i) => (
        <motion.div
          key={i}
          className="absolute text-rose-400"
          initial={{ y: -20, x: Math.random() * window.innerWidth, opacity: 0 }}
          animate={{ y: window.innerHeight + 50, opacity: [0, 1, 0] }}
          transition={{ duration: Math.random() * 5 + 4, repeat: Infinity, delay: Math.random() * 5 }}
        >
          ✨
        </motion.div>
      ))}

      {/* 헬로키티 이미지 (사용자가 public/kitty.png 넣어야 함) */}
      <motion.img
        src="/kitty.png"
        alt="Hello Kitty"
        className="w-32 h-32 mb-6 drop-shadow-xl"
        initial={{ scale: 0 }}
        animate={{ scale: 1, rotate: [0, 10, -10, 0] }}
        transition={{ duration: 1.2 }}
      />

      <h1 className="text-3xl font-bold text-rose-700 flex items-center gap-2">
        <Stars className="text-rose-500" /> 헬로키티 별자리 운세 <Stars className="text-rose-500" />
      </h1>

      <select
        className="mt-6 p-2 rounded-xl border-2 border-rose-400 text-rose-700 bg-white/80"
        value={sign}
        onChange={(e) => setSign(e.target.value)}
      >
        <option value="">별자리를 선택하세요</option>
        {Object.keys(fortunes).map((s) => (
          <option key={s} value={s}>
            {s}
          </option>
        ))}
      </select>

      <button
        onClick={handlePick}
        className="mt-4 px-6 py-2 bg-rose-500 text-white rounded-xl shadow hover:bg-rose-600 flex items-center gap-2"
      >
        <RefreshCw className="w-4 h-4" /> 운세 보기
      </button>

      {fortune && (
        <motion.div
          className="mt-6 p-4 rounded-2xl bg-white/80 shadow-lg text-center text-rose-700 text-lg max-w-xs space-y-2"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <div><Sparkles className="inline text-yellow-400 mr-2" /> {fortune.text}</div>
          <div>🎨 행운의 색: <span className="font-semibold">{fortune.color}</span></div>
          <div>✨ 행운의 행동: <span className="font-semibold">{fortune.action}</span></div>
        </motion.div>
      )}
    </div>
  );
}

