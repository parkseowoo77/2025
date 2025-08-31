import streamlit as st
import random
import time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# 🌸 전체 스타일 + 애니메이션
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 50%, #fad0c4 100%);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: white;
    font-family: 'Arial', sans-serif;
}
@keyframes gradientBG {
    0% {background-position:0% 50%}
    50% {background-position:100% 50%}
    100% {background-position:0% 50%}
}
.input-box {
    background: rgba(255,255,255,0.15);
    padding: 50px;
    border-radius: 25px;
    width: 50%;
    margin: auto;
    text-align: center;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.3);
}
input, button {
    font-size: 20px;
    padding: 12px;
    border-radius: 15px;
    border: none;
    outline: none;
}
button {
    background-color: #ff6b81;
    color: white;
    cursor: pointer;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}
.floating {
    position: fixed;
    top: -10px;
    font-size: 24px;
    animation: floatDown 3s linear infinite;
}
@keyframes floatDown {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# 🌟 시작 화면 하트/별/반짝이 배치
symbols = ["❤️", "⭐", "💖", "✨"]
colors = ["red","pink","yellow","white","purple","lightblue"]
floating_html = ""
for i in range(0, 100, 5):
    sym = random.choice(symbols)
    color = random.choice(colors)
    floating_html += f'<div class="floating" style="left:{i}%; color:{color};">{sym}</div>'
st.markdown(floating_html, unsafe_allow_html=True)

# 타이틀 + 입력 박스
st.title("💖 단어 궁합 테스트 💖")
st.markdown('<div class="input-box">', unsafe_allow_html=True)

word1 = st.text_input("첫 번째 단어를 입력하세요:")
word2 = st.text_input("두 번째 단어를 입력하세요:")

st.markdown('</div>', unsafe_allow_html=True)

# 점수 계산 및 효과
if st.button("궁합 보기 ✨"):
    if word1 and word2:
        ranges = [random.randint(i, i+9) for i in range(0, 100, 10)]
        score = random.choice(ranges)
        score_placeholder = st.empty()

        for i in range(score + 1):
            # 실시간 점수 증가
            score_placeholder.subheader(f"✨ {word1} ✨ + ✨ {word2} ✨ = ❤️ 궁합 {i}% ❤️")

            # 점수별 배경 색 변화
            if i <= 20:
                bg_color = "#2f2f2f"
            elif i <= 40:
                bg_color = "#4a6fa5"
            elif i <= 60:
                bg_color = "#ffe4b5"
            elif i <= 80:
                bg_color = "#ffb6c1"
            elif i <= 99:
                bg_color = "#ff69b4"
            else:
                bg_color = "rainbow"

            if bg_color != "rainbow":
                st.markdown(f"<style>body{{background-color:{bg_color};transition:background-color 0.3s linear;}}</style>", unsafe_allow_html=True)
            else:
                st.markdown("""
                <style>
                body {
                    background: linear-gradient(270deg, #ff0000, #ff9900, #ffff00, #33cc33, #3399ff, #9933ff, #ff3399);
                    background-size: 1400% 1400%;
                    animation: rainbowBG 5s ease infinite;
                }
                @keyframes rainbowBG {
                    0% {background-position:0% 50%}
                    50% {background-position:100% 50%}
                    100% {background-position:0% 50%}
                }
                </style>
                """, unsafe_allow_html=True)

            # 점수 비례 하트/별 증가
            floating_count = int(i/5) + 1
            dynamic_html = ""
            for n in range(floating_count):
                sym = random.choice(symbols)
                color = random.choice(colors)
                left = random.randint(0, 100)
                dynamic_html += f'<div class="floating" style="left:{left}%; color:{color};">{sym}</div>'
            st.markdown(dynamic_html, unsafe_allow_html=True)
            time.sleep(0.02)

        # 점수대별 음악 + 효과
        if score <= 20:
            st.warning(f"{score}% : 조금 서툰 궁합 🌫️")
            st.markdown('<audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/4384" type="audio/mpeg"></audio>', unsafe_allow_html=True)

        elif score <= 40:
            st.info(f"{score}% : 흐린 날씨 같은 궁합 🌧️")
            st.snow()
            st.markdown('<audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/387" type="audio/mpeg"></audio>', unsafe_allow_html=True)

        elif score <= 60:
            st.success(f"{score}% : 따뜻하고 달콤한 궁합 ☀️🌱")
            st.markdown('<audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/6678" type="audio/mpeg"></audio>', unsafe_allow_html=True)

        elif score <= 80:
            st.success(f"{score}% : 즐겁고 사랑스러운 궁합 🎶🎉")
            st.markdown('<audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/6677" type="audio/mpeg"></audio>', unsafe_allow_html=True)

        elif score <= 99:
            st.success(f"{score}% : 사랑이 넘치는 최고의 궁합 💖🎆")
            st.markdown('<audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/6292" type="audio/mpeg"></audio>', unsafe_allow_html=True)

        elif score == 100:
            st.success("🌈💖🎆🎉 세상에서 제일 화려한 궁합! 운명 그 자체 💍")
            st.balloons()
            st.snow()
            # 화면 가득 하트 + 폭죽 + 웨딩 음악
            st.markdown("""
            <style>
            .heart {position: fixed; top:-10px; font-size:28px; animation: fall 3s linear infinite;}
            @keyframes fall {0% {transform:translateY(0) rotate(0deg); opacity:1;} 100% {transform:translateY(100vh) rotate(360deg); opacity:0;}}
            </style>
            """, unsafe_allow_html=True)
            hearts_html = ""
            for left in range(0, 100, 3):
                color = random.choice(colors)
                hearts_html += f'<div class="heart" style="left:{left}%; color:{color}">❤️</div>'
            st.markdown(hearts_html, unsafe_allow_html=True)
            st.markdown("""
            <div style="position:fixed;top:0;left:0;width:100%;height:100%;background:url('https://i.imgur.com/xMXzQ9Z.gif') center/cover no-repeat;opacity:0.85;pointer-events:none;"></div>
            <audio autoplay><source src="https://www.fesliyanstudios.com/play-mp3/6679" type="audio/mpeg"></audio>
            """, unsafe_allow_html=True)

    else:
        st.warning("단어를 모두 입력해주세요!")
