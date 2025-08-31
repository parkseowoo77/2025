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
}
@keyframes rainbowSky {0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.centered {display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;}
h1 {color:white; font-size:6em; text-shadow:3px 3px 15px rgba(0,0,0,0.5); margin-bottom:40px; text-align:center;}
input {font-size:36px; padding:30px; border-radius:25px; border:3px solid #fff; text-align:center; width:200px; height:120px;}
.plus {font-size:50px; color:white; margin:0 20px; font-weight:bold; display:flex; align-items:center; justify-content:center;}
.equals {font-size:60px; color:white; font-weight:bold; margin:20px 10px; display:inline;}
.score_text {font-size:60px; color:white; font-weight:bold; display:inline;}
.result_text {font-size:48px; color:white; margin-top:15px;}
.fireworks_full {position:fixed; top:0; left:0; width:100%; height:100%; font-size:80px; text-align:center; animation:explode 1s ease;}
@keyframes explode {0% {opacity:1;} 100% {opacity:0; transform: scale(3);}}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)

# 입력 상자 + 기호
col1, col2, col3 = st.columns([1,0.1,1])
with col1:
    w1 = st.text_input("", key="word1", max_chars=15)
with col2:
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
with col3:
    w2 = st.text_input("", key="word2", max_chars=15)

st.markdown('<div style="margin-top:20px;"></div>', unsafe_allow_html=True)

# 즉석 이유 생성
def generate_reason(score, w1, w2):
    if score <= 20:
        return f"'{w1}'이랑 '{w2}'… 같이 있어도 마치 서로 다른 영화 보는 기분 😢😂"
    elif score <= 40:
        return f"'{w1}' + '{w2}'… 오잉? 같이하면 웃음 폭발! 근데 약간 엉뚱함 😂🎬"
    elif score <= 60:
        return f"'{w1}'과 '{w2}'… 서로 장난치면서 깔깔거리기 딱 좋은 조합 😆🍿"
    elif score <= 80:
        return f"'{w1}' + '{w2}'… 달콤함 폭발! 손잡으면 주변이 무지개 🌈💞"
    elif score <= 99:
        return f"'{w1}'과 '{w2}'… 심쿵 심쿵! 하트와 별이 팡팡 💖✨"
    else:
        return f"'{w1}' + '{w2}'… 천생연분! 💍 신랑👰와 신부🤵 등장! 하트/꽃 폭발 💖🌸💥"

# 궁합 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    score_placeholder = st.empty()
    desc_placeholder = st.empty()
    score = random.randint(0,100)
    for i in range(score+1):
        score_placeholder.markdown(f'<div class="equals">=</div><span class="score_text"> {i}%</span>', unsafe_allow_html=True)
        desc_placeholder.markdown(f'<div class="result_text">{generate_reason(i, w1, w2)}</div>', unsafe_allow_html=True)
        # 점수별 화면 전체 폭죽/하트 한번 터짐
        if i>50 and i<100 and i%20==0:
            st.markdown('<div class="fireworks_full">💖✨🎆🎇💖✨🎆🎇</div>', unsafe_allow_html=True)
        time.sleep(0.02)
    if score == 100:
        st.markdown("""
        <div style='text-align:center; margin-top:20px;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='150'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='150'>
            <p style='font-size:60px;color:red;'>💖 신랑과 신부 등장! 💖</p>
            <div class="fireworks_full">💖✨🎆🎇💖✨🎆🎇💖✨🎆🎇</div>
        </div>
        """, unsafe_allow_html=True)
