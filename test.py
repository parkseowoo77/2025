import streamlit as st
import random, time

st.set_page_config(page_title="💖단어 궁합 앱💖", layout="wide")

# 스타일: 무지개 하늘 + 중앙 정렬 + 제목/입력글씨 크게
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
input {font-size:28px; padding:18px; border-radius:20px; border:3px solid #fff; text-align:center; width:250px;}
.button {font-size:22px; padding:15px 30px; border-radius:20px; background:#ff6b81; color:white; border:none; cursor:pointer; margin-top:20px;}
.label {font-size:28px; color:white; font-weight:bold; margin-bottom:10px;}
.plus {font-size:40px; color:white; margin:0 15px; font-weight:bold;}
.equals {font-size:50px; color:white; font-weight:bold; margin:20px 0;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)

# 입력 상자와 + 기호
col1, col2, col3 = st.columns([1,0.2,1])
with col1:
    w1 = st.text_input("", key="word1", max_chars=15, help="첫 번째 단어")
with col2:
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
with col3:
    w2 = st.text_input("", key="word2", max_chars=15, help="두 번째 단어")

st.markdown('<div class="equals">=</div>', unsafe_allow_html=True)

# 단어 특성
def traits(word):
    d = {"초코":["달콤","쫀득"],"커피":["쌉쌀","뜨거움"],"사과":["상큼","발랄"],
         "바나나":["부드럽","노랗"],"햄버거":["기름짐","배부름"],"피자":["치즈폭발","중독성"]}
    return d.get(word, ["평범","신비"])

# 웃긴 설명
def funny(score,w1,w2):
    r=f"{w1}({random.choice(traits(w1))}) + {w2}({random.choice(traits(w2))})"
    if score<=20: return f"{r}… 갑자기 춤추고 싶어지는 조합! 💃😂"
    elif score<=40: return f"{r}… 노래방에서 소리 지를 것 같은 커플 🎤🤣"
    elif score<=60: return f"{r}… 같이 치킨 먹으면서 깔깔 웃게 되는 조합 🍗😆"
    elif score<=80: return f"{r}… 달콤쌉쌀 폭발! 🍫☕ 친구들이 부러워할 조합 😍"
    elif score<=99: return f"{r}… 하트와 별이 동시에 터지는 조합 💖✨ 모두 심쿵 💥"
    else: return f"{r}… 천생연분! 💍 신랑👰와 신부🤵 등장! 하트/꽃 폭발 💖🌸💥"

# 궁합 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    score_placeholder=st.empty()
    desc_placeholder=st.empty()
    score=random.randint(0,100)
    for i in range(score+1):
        score_placeholder.subheader(f"✨ {w1} + {w2} = ❤️ 궁합 {i}% ❤️")
        desc_placeholder.markdown(f"💬 {funny(i,w1,w2)}")
        time.sleep(0.02)
    if score==100:
        st.markdown("""
        <div style='text-align:center;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='150'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='150'>
            <p style='font-size:40px;color:red;'>💖 신랑과 신부 등장! 💖</p>
        </div>
        """, unsafe_allow_html=True)
