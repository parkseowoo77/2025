import streamlit as st
import random

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
.result_text {font-size:40px; color:white; margin-top:15px; line-height:1.5;}
.effect_item {position:fixed; font-size:50px; animation:flyRotate 1s ease forwards;}
@keyframes flyRotate {0% {opacity:1; transform:translateY(0) rotate(0deg);}100% {opacity:0; transform:translateY(-300px) rotate(720deg) scale(2);}}
</style>
""", unsafe_allow_html=True)

# 화면 맨 위 제목과 입력 상자
st.markdown('<div class="top_centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)

# 입력 상자 + 기호
col1, col2, col3 = st.columns([1,0.1,1])
with col1:
    w1 = st.text_input("첫 번째 단어", key="word1", max_chars=15)
with col2:
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
with col3:
    w2 = st.text_input("두 번째 단어", key="word2", max_chars=15)
st.markdown('</div>', unsafe_allow_html=True)

# 폭발 효과
def generate_effect_list(score):
    if score <= 20: return ["☔","🌧️","💧"]
    elif score <= 40: return ["💦","💧"]
    elif score <= 60: return ["💖","✨"]
    elif score <= 80: return ["🌈","💖","🎉"]
    elif score <= 99: return ["💖","🎆","🎇","✨"]
    else: return ["💖","✨","🎆","🎇","💍","💞","🌸"]

def show_explosion(score, count=30):
    effects = generate_effect_list(score)
    for _ in range(count):
        e = random.choice(effects)
        left = random.randint(0,90)
        top = random.randint(10,90)
        size = random.randint(50,120)
        st.markdown(f"""
        <div class="effect_item" style="left:{left}%; top:{top}%; font-size:{size}px;">{e}</div>
        """, unsafe_allow_html=True)

# 긴 웃긴 이유 생성
def generate_long_funny_reason(score, w1, w2):
    templates_low = [
        f"'{w1}'과 '{w2}'? 음… 둘 다 서로를 보고 눈치만 살피네요. 결국 둘 다 소파 구석으로 도망쳤어요. 😢\n근데 사실 '{w1}'은 간식이 더 궁금하고, '{w2}'는 햇빛이 더 좋아요.\n서로 한 발짝도 못 다가가네요. 정말 비극적이지만 웃겨요. 아마 둘 다 비 오는 날 우산 하나로 겨우 버티는 느낌?\n솔직히, 다음에는 핫초코라도 준비해야 할 듯!"
    ]
    templates_mid = [
        f"'{w1}'과 '{w2}'… 서로 장난치면서 웃음이 끊이질 않아요. 😂\n'{w1}'이 작은 장난을 던지면 '{w2}'는 바로 대응! 눈치 싸움 승자는? 아무도 몰라요.\n간혹 서로 깜짝 놀라면서도, 결국 장난감 하나씩 나눠 가지는 사이.\n서로에 대한 이해는 살짝 부족하지만, 순간순간 귀여움 폭발!"
    ]
    templates_high = [
        f"'{w1}' + '{w2}'… 하트 폭발! 💖\n눈 마주치면 심쿵! 매번 같이 있을 때마다 별이 튀어나오는 느낌 🌟\n둘 다 장난꾸러기지만 서로를 너무 잘 아는 느낌.\n이 조합은 정말 달콤한 폭죽처럼 폭발적이에요. 사랑이 팡팡 터지는 느낌!"
    ]
    templates_perfect = [
        f"'{w1}' + '{w2}'… 완벽한 천생연분! 💍\n신랑👰과 신부🤵 등장! 온 세상이 폭죽과 꽃으로 뒤덮이는 마법 같은 순간 💖🌸💥\n둘이 손 잡는 순간, 하트와 별이 팡팡! 주변 사람들도 심쿵!\n이 조합은 그냥 단어계의 신데렐라와 프린스 찰떡궁합.\n서로의 장점을 100% 살려주는 완벽한 콤비!"
    ]
    if score <= 40: return random.choice(templates_low)
    elif score <= 70: return random.choice(templates_mid)
    elif score <= 99: return random.choice(templates_high)
    else: return random.choice(templates_perfect)

# 궁합 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    score = random.randint(0,100)
    st.markdown(f'<div class="equals">=</div><span class="score_text"> {score}%</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="result_text">{generate_long_funny_reason(score, w1, w2)}</div>', unsafe_allow_html=True)
    show_explosion(score, count=50)

    if score == 100:
        st.markdown("""
        <div style='text-align:center; margin-top:20px;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='180'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='180'>
            <p style='font-size:60px;color:red;'>💖 신랑과 신부 등장! 💖</p>
        </div>
        """, unsafe_allow_html=True)
        show_explosion(score, count=50)
