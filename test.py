import streamlit as st
import random, time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# 스타일: 무지개 하늘 + 중앙 정렬 + 입력창 크게
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #87CEEB, #ff9a9e, #a18cd1, #fbc2eb, #89f7fe);
    background-size: 400% 400%;
    animation: rainbowSky 20s ease infinite;
}
@keyframes rainbowSky {0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.centered {display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;}
h1 {color:white; font-size:4em; text-shadow:2px 2px 12px rgba(0,0,0,0.5); margin-bottom:30px;}
input {font-size:22px; padding:15px; border-radius:15px; border:3px solid #fff; text-align:center; width:350px; margin-bottom:20px;}
button {font-size:20px; padding:12px 25px; border-radius:15px; background:#ff6b81; color:white; border:none; cursor:pointer;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)
w1 = st.text_input("첫 번째 단어를 입력하세요:")
w2 = st.text_input("두 번째 단어를 입력하세요:")
st.markdown('</div>', unsafe_allow_html=True)

# 단어 특성
def traits(word):
    d = {"초코":["달콤","쫀득"],"커피":["쌉쌀","뜨거움"],"사과":["상큼","발랄"],
         "바나나":["부드럽","노랗"],"햄버거":["기름짐","배부름"],"피자":["치즈폭발","중독성"]}
    return d.get(word, ["평범","신비"])

# 웃긴 설명
def funny(score,w1,w2):
    r=f"{w1}({random.choice(traits(w1))}) + {w2}({random.choice(traits(w2))})"
    if score<=20: return f"{r}… 너무 달라서 우주도 '뭐야 이 커플?' 🌌😂"
    elif score<=40: return f"{r}… 장난치다 엉덩방아! 🐘🤣"
    elif score<=60: return f"{r}… 서로 맛을 알아가는 중 🍫☕"
    elif score<=80: return f"{r}… 달콤쌉쌀 조합 완성! 😍"
    elif score<=99: return f"{r}… 레전드 커플 직전! 💖"
    else: return f"{r}… 천생연분! 💍 신랑👰와 신부🤵 등장! 💖🌸💥"

if st.button("궁합 보기 ✨") and w1 and w2:
    score_placeholder=st.empty()
    desc_placeholder=st.empty()
    score=random.randint(0,100)
    for i in range(score+1):
        score_placeholder.subheader(f"✨ {w1} + {w2} = ❤️ 궁합 {i}% ❤️")
        desc_placeholder.markdown(f"💬 {funny(i,w1,w2)}")
        time.sleep(0.02)
    # 100점 특별 화면
    if score==100:
        st.markdown("""
        <div style='text-align:center;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='150'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='150'>
            <p style='font-size:40px;color:red;'>💖 신랑과 신부 등장! 💖</p>
        </div>
        """, unsafe_allow_html=True)
