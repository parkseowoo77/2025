import streamlit as st
import random
import time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# 🌸 전체 스타일
st.markdown("""
<style>
body {
    margin:0;
    padding:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: white;
    font-family: 'Arial', sans-serif;
    overflow: hidden;
}
@keyframes gradientBG {
    0% {background-position:0% 50%}
    50% {background-position:100% 50%}
    100% {background-position:0% 50%}
}
.container {
    text-align: center;
    z-index: 10;
}
h1 {
    font-size: 3em;
    margin-bottom: 20px;
    text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
}
.input-box {
    background: rgba(255,255,255,0.2);
    padding: 50px;
    border-radius: 30px;
    width: 400px;
    margin: auto;
    text-align: center;
    box-shadow: 0 15px 30px rgba(0,0,0,0.3);
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.3);
}
input, button {
    font-size: 18px;
    padding: 12px;
    border-radius: 12px;
    border: none;
    outline: none;
    margin-top: 10px;
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
    top: -50px;
    font-size: 24px;
    animation: floatDown 4s linear infinite;
    z-index: 0;
}
@keyframes floatDown {
    0% { transform: translateY(0) rotate(0deg); opacity: 1; }
    100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

# 하늘에서 떨어지는 하트/별/반짝이
symbols = ["❤️", "⭐", "💖", "✨", "💥", "🔥"]
colors = ["red","pink","yellow","white","purple","lightblue"]
floating_html = ""
for i in range(0, 100, 5):
    sym = random.choice(symbols)
    color = random.choice(colors)
    left = random.randint(0, 100)
    floating_html += f'<div class="floating" style="left:{left}%; color:{color};">{sym}</div>'
st.markdown(floating_html, unsafe_allow_html=True)

# 중앙 컨테이너
st.markdown('<div class="container">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)
st.markdown('<div class="input-box">', unsafe_allow_html=True)

word1 = st.text_input("첫 번째 단어를 입력하세요:")
word2 = st.text_input("두 번째 단어를 입력하세요:")

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# 단어 속성 매핑
def get_word_traits(word):
    traits = {
        "초코": ["달콤", "쫀득", "장난꾸러기"],
        "커피": ["쌉쌀", "뜨거움", "활력"],
        "사과": ["상큼", "발랄", "건강"],
        "바나나": ["부드럽", "노랗", "유머감각"],
        "햄버거": ["기름짐", "배부름", "행복"],
        "피자": ["치즈폭발", "중독성", "파티감각"],
        # 필요하면 단어 더 추가 가능
    }
    return traits.get(word, ["평범", "신비", "알수없음"])

# 즉석 코믹 설명 생성
def generate_funny_description(score, w1, w2):
    traits1 = get_word_traits(w1)
    traits2 = get_word_traits(w2)
    
    # 점수별 상황
    if score <= 20:
        reason = f"{w1}({random.choice(traits1)})와 {w2}({random.choice(traits2)})… 서로 너무 달라서 초코처럼 싸우고 커피처럼 쌉싸름! 🥋😂"
        description = f"길거리에서 {w1}가 {w2}에게 돌진하고, 지나가던 강아지는 '뭐야 이거?' 🐶💨"
    elif score <= 40:
        reason = f"{w1}({random.choice(traits1)})가 {w2}({random.choice(traits2)})에게 장난치지만, {w2}는 쌉싸름하게 반응 🤧💥"
        description = f"{w1}가 {w2}에게 포옹하려다 엉덩방아! 🐘🤣 지나가던 고양이도 심장 터질 뻔 🐱"
    elif score <= 60:
        reason = f"{w1}와 {w2}는 서로 맛을 알아가는 중 🍫☕ 둘이 섞이면 살짝 혼란 🌪️"
        description = f"주변 친구들: '케이크 만들고 있는 거냐?' 🎂🤣 바람 불면 둘이 하늘로 날아감 🪁💨"
    elif score <= 80:
        reason = f"달콤쌉쌀 조합 완성! 😍 {w1} 웃으면 {w2} 심쿵 💣✨"
        description = "장난치다 폭발, 주변 사람들: '대피! 불났다!' 🔥🏃‍♂️💨 강아지도 귀여워서 놀람 🐶"
    elif score <= 99:
        reason = f"레전드 커플 직전! 💖 {w1}+{w2}, 달콤+쌉쌀+웃음 폭발 🌈💥"
        description = "둘이 웃으면 주변 사람들 기절 😵‍💫 하늘에서 별이 떨어지고, 꽃들도 둘을 향해 고개 끄덕임 🌸🌟"
    else:
        reason = f"와우… {w1}+{w2}, 천생연분 레벨 💍🍫☕ 달콤+쌉쌀 폭발 😆💥"
        description = "주변 사람들: 웃음+눈물+심쿵 😂😭💖 고양이, 강아지, 토끼: '이 커플 레전드!' 🐱🐶🐇 UFO 등장 👽✨"
    
    return reason, description

# 궁합 버튼
if st.button("궁합 보기 ✨"):
    if word1 and word2:
        score_placeholder = st.empty()
        reason_placeholder = st.empty()
        desc_placeholder = st.empty()
        
        # 점수 랜덤 생성
        score = random.randint(0,100)

        # 실시간 점수 증가
        for i in range(score + 1):
            score_placeholder.subheader(f"✨ {word1} ✨ + ✨ {word2} ✨ = ❤️ 궁합 {i}% ❤️")
            
            reason, desc = generate_funny_description(i, word1, word2)
            reason_placeholder.markdown(f"📌 이유: {reason}")
            desc_placeholder.markdown(f"💬 설명: {desc}")

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
                @keyframes rainbow
