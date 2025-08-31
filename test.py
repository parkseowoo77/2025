import streamlit as st
import random, time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# CSS
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #87CEEB, #ff9a9e, #a18cd1, #fbc2eb, #89f7fe);
    background-size: 400% 400%;
    animation: rainbowSky 20s ease infinite;
    overflow:hidden;
    height:100vh;
}
@keyframes rainbowSky {0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.top_centered {display:flex; flex-direction:column; justify-content:flex-start; align-items:center; text-align:center; padding-top:30px;}
h1 {color:white; font-size:6em; text-shadow:3px 3px 15px rgba(0,0,0,0.5); margin-bottom:40px; text-align:center;}
input {font-size:60px; padding:60px; border-radius:30px; border:3px solid #fff; text-align:center; width:300px; height:200px; margin-bottom:20px;}
.plus {font-size:50px; color:white; margin:0 20px; font-weight:bold; display:flex; align-items:center; justify-content:center;}
.equals {font-size:60px; color:white; font-weight:bold; margin:20px 10px; display:inline;}
.score_text {font-size:60px; color:white; font-weight:bold; display:inline;}
.result_text {font-size:48px; color:white; margin-top:15px;}
.effect_item {
    position:fixed; font-size:50px; animation:flyRotate 1s ease forwards;
}
@keyframes flyRotate {
    0% {opacity:1; transform:translateY(0) rotate(0deg);}
    100% {opacity:0; transform:translateY(-300px) rotate(720deg) scale(2);}
}
</style>
""", unsafe_allow_html=True)

# 화면 맨 위에 제목과 입력 상자
st.markdown('<div class="top_centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)

# 입력 상자 + 기호
col1, col2, col3 = st.columns([1,0.1,1])
with col1:
    w1 = st.text_input("", key="word1", max_chars=15)
with col2:
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
with col3:
    w2 = st.text_input("", key="word2", max_chars=15)
st.markdown('</div>', unsafe_allow_html=True)

# 점수별 이유
def generate_reason(score, w1, w2):
    if score <= 20:
        return f"'{w1}'과 '{w2}'… 마음은 비오는 날처럼 😢🌧️"
    elif score <= 40:
        return f"'{w1}' + '{w2}'… 웃기지만 약간 엉뚱함 😂🌦️"
    elif score <= 60:
        return f"'{w1}'과 '{w2}'… 장난치며 깔깔거리기 딱 좋아 😆✨"
    elif score <= 80:
        return f"'{w1}' + '{w2}'… 달콤 폭발! 🌈💖"
    elif score <= 99:
        return f"'{w1}'과 '{w2}'… 심쿵! 하트와 별 팡팡 💖✨"
    else:
        return f"'{w1}' + '{w2}'… 천생연분! 💍 신랑👰와 신부🤵 등장! 하트/꽃 폭발 💖🌸💥"

# 점수별 효과 이모지 리스트
def generate_effect_list(score):
    if score <= 20:
        return ["☔","🌧️","💧"]
    elif score <= 40:
        return ["💦","💧"]
    elif score <= 60:
        return ["💖","✨"]
    elif score <= 80:
        return ["🌈","💖","🎉"]
    elif score <= 99:
        return ["💖","🎆","🎇","✨"]
    else:
        return ["💖","✨","🎆","🎇","💍","💞","🌸"]

# 화면에 효과 무작위 생성
def show_effect(score, count=30):
    effects = generate_effect_list(score)
    for _ in range(count):
        e = random.choice(effects)
        left = random.randint(0,90)
        top = random.randint(10,90)
        size = random.randint(50,120)
        st.markdown(f"""
        <div class="effect_item" style="left:{left}%; top:{top}%; font-size:{size}px;">{e}</div>
        """, unsafe_allow_html=True)

# 궁합 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    score_placeholder = st.empty()
    desc_placeholder = st.empty()
    score = random.randint(0,100)
    for i in range(score+1):
        score_placeholder.markdown(f'<div class="equals">=</div><span class="score_text"> {i}%</span>', unsafe_allow_html=True)
        desc_placeholder.markdown(f'<div class="result_text">{generate_reason(i, w1, w2)}</div>', unsafe_allow_html=True)
        show_effect(i, count=5)
        time.sleep(0.02)
    if score == 100:
        # 신랑/신부 이미지와 여러 레이어 폭발
        st.markdown("""
        <div style='text-align:center; margin-top:20px;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='180'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='180'>
            <p style='font-size:60px;color:red;'>💖 신랑과 신부 등장! 💖</p>
        </div>
        """, unsafe_allow_html=True)
        for _ in range(5):
            show_effect(score, count=50)
            time.sleep(0.1)
