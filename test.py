import streamlit as st
import random
import time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# 스타일: 배경 + 중앙 정렬 + 입력창 + 하트/별 애니메이션
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #87CEEB, #ff9a9e, #a18cd1, #fbc2eb, #89f7fe);
    background-size: 400% 400%;
    animation: rainbowSky 20s ease infinite;
}
@keyframes rainbowSky {
    0% {background-position:0% 50%}
    50% {background-position:100% 50%}
    100% {background-position:0% 50%}
}
.centered {
    display: flex; justify-content: center; align-items: center; flex-direction: column;
    height: 100vh;
}
h1 {
    text-align: center; 
    color: white; 
    font-size: 3em; 
    text-shadow: 2px 2px 12px rgba(0,0,0,0.5);
    margin-bottom: 30px;
}
input {
    font-size: 18px; 
    padding: 10px; 
    border-radius: 10px; 
    border: 2px solid #fff; 
    outline: none;
    text-align: center;
    width: 250px;
    margin-bottom: 10px;
}
button {
    background-color: #ff6b81; 
    color: white; 
    font-weight: bold; 
    cursor: pointer; 
    font-size: 18px;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
}
.floating {position: fixed; top: -50px; font-size: 24px; animation: floatDown 4s linear infinite; z-index: 0;}
@keyframes floatDown {0% { transform: translateY(0) rotate(0deg); opacity: 1;} 100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }}
</style>
""", unsafe_allow_html=True)

# 하트/별 떨어지는 효과
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
st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)
word1 = st.text_input("첫 번째 단어를 입력하세요:")
word2 = st.text_input("두 번째 단어를 입력하세요:")
st.markdown('</div>', unsafe_allow_html=True)

# 단어 특성 예시
def get_word_traits(word):
    traits = {
        "초코": ["달콤", "쫀득", "장난꾸러기"],
        "커피": ["쌉쌀", "뜨거움", "활력"],
        "사과": ["상큼", "발랄", "건강"],
        "바나나": ["부드럽", "노랗", "유머감각"],
        "햄버거": ["기름짐", "배부름", "행복"],
        "피자": ["치즈폭발", "중독성", "파티감각"],
    }
    return traits.get(word, ["평범", "신비", "알수없음"])

# 웃긴 설명 생성
def generate_funny_description(score, w1, w2):
    traits1 = get_word_traits(w1)
    traits2 = get_word_traits(w2)
    reason = f"{w1}({random.choice(traits1)}) + {w2}({random.choice(traits2)})"
    description = ""
    
    if score <= 20:
        description = f"{reason}… 서로 너무 달라서 우주도 '뭐야 이 커플?' 🌌😂 길거리 코미디 폭발, 지나가던 강아지 기절 🐶💨"
    elif score <= 40:
        description = f"{reason}… 장난치다 엉덩방아! 🐘🤣 주변 고양이: '또 뭐야?' 🐱 점심 도시락 폭발 🍱💥"
    elif score <= 60:
        description = f"{reason}… 서로 맛을 알아가는 중 🍫☕ 친구들: '케이크 만들고 있어?' 🎂🤣 바람 불면 둘이 날아감 🪁"
    elif score <= 80:
        description = f"{reason}… 달콤쌉쌀 조합 완성! 😍 웃으면 주변 사람들 심쿵 💣✨ 장난치다 폭발 🔥🏃‍♂️"
    elif score <= 99:
        description = f"{reason}… 레전드 커플 직전! 💖 웃으면 주변 기절 😵‍💫 별 떨어지고 꽃 고개 끄덕임 🌸🌟 UFO도 지나감 👽✨"
    else:  # 100점
        description = f"{reason}… 천생연분! 💍 신랑👰와 신부🤵 등장, 하트와 꽃 폭발 💖🌸💥 모두 박수 👏🎉 폭죽 터지고 모든 사람들이 감탄함 😆"
    return description

# 궁합 버튼
if st.button("궁합 보기 ✨"):
    if word1 and word2:
        score_placeholder = st.empty()
        desc_placeholder = st.empty()
        score = random.randint(0,100)

        for i in range(score+1):
            score_placeholder.subheader(f"✨ {word1} ✨ + ✨ {word2} ✨ = ❤️ 궁합 {i}% ❤️")
            description = generate_funny_description(i, word1, word2)
            desc_placeholder.markdown(f"💬 {description}")

            # 점수별 배경
            if i <= 20: bg_color = "#a0c4ff"
            elif i <= 40: bg_color = "#bdb2ff"
            elif i <= 60: bg_color = "#ffc6ff"
            elif i <= 80: bg_color = "#ffadad"
            elif i <= 99: bg_color = "#ffd6a5"
            else: 
                # 100점 결혼식 장면
                st.markdown("""
                <style>
                body {background: linear-gradient(to top, #87ceeb, #ffffff);}
                .wedding {text-align:center;}
                </style>
                <div class="wedding">
                    <img src="https://i.ibb.co/2Zr91gF/bride.png" width="100" style="animation: floatDown 5s linear infinite;">
                    <img src="https://i.ibb.co/7Yw2gFt/groom.png" width="100" style="animation: floatDown 5s linear infinite;">
                    <p style="font-size:30px; color:red;">💖 신랑과 신부 등장! 💖</p>
                </div>
                """, unsafe_allow_html=True)
            time.sleep(0.02)
