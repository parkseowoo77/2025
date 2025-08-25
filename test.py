import React, { useState } from "react";
import { motion } from "framer-motion";

const fortunes = [
  { text: "활력이 샘솟는 하루!", color: "핑크", action: "새 목표 1가지 적기" },
  { text: "꾸준함의 힘이 보이는 날", color: "초록", action: "루틴 체크\u2714" },
  { text: "대화운 상승!", color: "노랑", action: "친구에게 안부 톡" },
  { text: "마음이 말랑해지는 날", color: "하늘색", action: "감사 메시지 보내기" },
];

function getFortune(dateStr) {
  try {
    const d = new Date(dateStr);
    if (isNaN(d)) return null;
    const idx = (d.getMonth() + d.getDate()) % fortunes.length;
    return fortunes[idx];
  } catch {
    return null;
  }
}

export default function BirthdayFortune() {
  const [birthday, setBirthday] = useState("");
  const [fortune, setFortune] = useState(null);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-pink-100 p-6">
      <h1 className="text-2xl font-bold text-rose-700 mb-4">
        {"\u{1F382}\u{1F431}\u{1F436} "}생일 운세{" \u{1F389}"}
      </h1>
      <input
        type="date"
        value={birthday}
        onChange={(e) => setBirthday(e.target.value)}
        className="px-3 py-2 rounded-xl border mb-3"
      />
      <button
        onClick={() => setFortune(getFortune(birthday))}
        className="px-4 py-2 rounded-xl bg-rose-500 text-white"
      >
        운세 보기
      </button>
      {fortune && (
        <motion.div
          className="mt-4 p-4 bg-white rounded-xl shadow text-center"
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
        >
          <p>{"\u{1F4AB} "}{fortune.text}</p>
          <p>{"\u{1F3A8} "}행운의 색: {fortune.color}</p>
          <p>{"\u2728 "}행운의 행동: {fortune.action}</p>
          <p className="mt-2 text-2xl">{"\u{1F496}\u{1F389}\u{1F431}\u{1F436}\u{1F382}"}</p>
        </motion.div>
      )}
    </div>
  );
}
