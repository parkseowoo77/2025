import streamlit as st
import random, time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# CSS 스타일
st.markdown("""
<style>
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #87CEEB, #ff9a9e, #a18cd1, #fbc2eb, #89f7fe);
    background-size: 400% 400%;
    animation: rainbowSky 20s ease infinite;
}
@keyframes rainbowSky {0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.centered {display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh; text-align:center;}
h1 {color:white; font-size:6em; text-shadow:3px 3px 15px rgba(0,0,0,0.5); margin-bottom:40px;}
input {font-size:32px; padding:25px; border-radius:25px; border:3px solid #fff; text-align:center; width:300px;}
.plus {font-size:50px; color:white; margin:0 20px; font-weight:bold; display:flex; align-items:center; justify-content:center;}
.equals {font-size:50px; color:white; font-weight:bold; margin:20px 10px; display:inline;}
.score_text {font-size:40px; color:white; font-weight:bold; display:inline;}
.result_text {font-size:32px; color:white; margin-top:15px;}
.hearts, .fireworks {position:absolute; font-size:40px; animation:floatUp 2s linear infinite;}
@keyframes floatUp {0% {transform: translateY(0px);} 100% {transform: translateY(-600px);}}
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

# 단어 특성
def traits(word):
    d = {"초코":["달콤","쫀득"],"커피":["쌉쌀","뜨거움"],"사과":["상큼","발랄"],
         "바나나":["부드럽","노랗"],"햄버거":["기름짐","배부름"],"피자":["치즈폭발","중독성"]}
    return d.get(word, ["평범","신비"])

# 점수별 웃긴 이유
def funny(score,w1,w2):
    r=f"{w1}({random.choice(traits(w1))}) + {w2}({random.choice(traits(w2))})"
    low = [f"{r}… 갑자기 춤추고 싶어지는 조합! 💃😂",
           f"{r}… 길거리에서 즉흥 공연할 것 같은 느낌 🎤🤣",
           f"{r}… 고양이도 깜짝 놀랄 궁합 🐱😹",
           f"{r}… 혼자 방에서 빵 터질 조합 😆"]
    mid = [f"{r}… 같이 치킨 먹으며 깔깔 웃게 되는 조합 🍗😆",
           f"{r}… 영화관에서 팝콘 던질지도 🍿🤣",
           f"{r}… 친구들이 '둘 왜 이렇게 웃기냐?' 😎😂",
           f"{r}… 서로 간식 나눠먹으며 폭소 😋😂"]
    high = [f"{r}… 달콤쌉쌀 폭발! 🍫☕ 심쿵 💖",
            f"{r}… 하트와 별이 동시에 터지는 조합 💖✨",
            f"{r}… 손잡으면 주변이 무지개 🌈💞",
            f"{r}… 같이 여행가면 웃음 폭발 🏖️😆"]
    if score<=20: return random.choice(low)
    elif score<=40: return random.choice(low+mid)
    elif score<=60: return random.choice(mid)
    elif score<=80: return random.choice(mid+high)
    elif score<=99: return random.choice(high)
    else: return f"{r}… 천생연분! 💍 신랑👰와 신부🤵 등장! 하트/꽃 폭발 💖🌸💥"

# 궁합 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    score_placeholder=st.empty()
    desc_placeholder=st.empty()
    score=random.randint(0,100)
    for i in range(score+1):
        # 점수 = 옆에 표시
        score_placeholder.markdown(f'<div class="equals">=</div><span class="score_text"> {i}%</span>', unsafe_allow_html=True)
        # 이유
        desc_placeholder.markdown(f'<div class="result_text">{funny(i,w1,w2)}</div>', unsafe_allow_html=True)
        # 점수별 하트/폭죽 텍스트 애니메이션
        if i>50 and i<100:
            st.markdown('<div class="hearts">💖✨💖✨🎆🎇</div>', unsafe_allow_html=True)
        time.sleep(0.02)
    if score==100:
        st.markdown("""
        <div style='text-align:center; margin-top:20px;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='150'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='150'>
            <p style='font-size:50px;color:red;'>💖 신랑과 신부 등장! 💖</p>
            <div class="hearts">💖✨💖✨🎆🎇💖✨💖✨</div>
        </div>
        """, unsafe_allow_html=True)
