import streamlit as st
import random
import time

st.set_page_config(page_title="💖단어 궁합 테스트💖", layout="wide")

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
.top_centered {display:flex; flex-direction:column; justify-content:flex-start; align-items:center; text-align:center; padding-top:20px;}
h1 {color:white; font-size:5em; text-shadow:3px 3px 15px rgba(0,0,0,0.5); margin-bottom:20px; text-align:center;}
input {font-size:50px; padding:60px; border-radius:30px; border:3px solid #fff; text-align:center; width:300px; height:180px; margin-bottom:20px;}
.plus {font-size:50px; color:white; margin:0 20px; font-weight:bold; display:flex; align-items:center; justify-content:center;}
.equals {font-size:60px; font-weight:bold; margin:20px 10px; display:inline;}
.score_text {font-size:60px; font-weight:bold; display:inline;}
.result_text {font-size:30px; margin-top:15px; line-height:1.5; text-align:center;}
.effect_item {position:fixed; font-size:50px; animation:flyRotate 5s ease forwards;}
@keyframes flyRotate {0% {opacity:1; transform:translateY(0) rotate(0deg);}100% {opacity:0; transform:translateY(-500px) rotate(720deg) scale(2);}}
</style>
""", unsafe_allow_html=True)

# 제목과 입력
st.markdown('<div class="top_centered">', unsafe_allow_html=True)
st.markdown("<h1>💖 단어 궁합 테스트 💖</h1>", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,0.1,1])
with col1:
    w1 = st.text_input("첫 번째 단어", key="word1", max_chars=15)
with col2:
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
with col3:
    w2 = st.text_input("두 번째 단어", key="word2", max_chars=15)
st.markdown('</div>', unsafe_allow_html=True)

# 결과 placeholder
result_placeholder = st.empty()
score_placeholder = st.empty()
effect_placeholder = st.empty()

# 점수별 효과
def generate_effect_list(score):
    if score <= 20: return ["☔","🌧️","💧"]
    elif score <= 40: return ["💦","💧"]
    elif score <= 60: return ["💖","✨"]
    elif score <= 80: return ["🌈","💖","🎉"]
    elif score <= 99: return ["💖","🎆","🎇","✨"]
    else: return ["💖","✨","🎆","🎇","💍","💞","🌸"]

def show_explosion(score, count=50):
    effects_html = ""
    effects = generate_effect_list(score)
    for _ in range(count):
        e = random.choice(effects)
        left = random.randint(0,90)
        top = random.randint(10,90)
        size = random.randint(50,120)
        effects_html += f"""
        <div class="effect_item" style="left:{left}%; top:{top}%; font-size:{size}px;">{e}</div>
        """
    effect_placeholder.markdown(effects_html, unsafe_allow_html=True)
    time.sleep(5)
    effect_placeholder.empty()

# 대화식 이유 생성
def generate_long_funny_reason(score, w1, w2):
    if score <= 40:
        templates_low = [
            f"'{w1}': '어… 너 왜 거기 있어?' 😢\n"
            f"'{w2}': '나? 그냥 햇빛 좀 쬐려고… 근데 너도 있네.'\n"
            f"'{w1}': '아, 그… 나 간식 먹고 있었는데…' \n"
            f"둘은 서로를 보지만 눈치만 보고 있어요. 결국 아무 일도 안 일어나고, 가끔 서로 이상한 표정만 주고받아요. "
            f"그래도 어쩐지 귀엽게 엉뚱한 행동으로 웃음을 줍니다."
        ]
        return random.choice(templates_low)
    elif score <= 70:
        templates_mid = [
            f"'{w1}': '이 장난감 내가 먼저 잡았다!' 😂\n"
            f"'{w2}': '어, 그럼 나도 하나 가져갈래!' \n"
            f"둘이 서로 장난을 치며 놀다가 갑자기 심쿵할 때도 있어요. "
            f"서로 깜짝 놀라며 웃고, 가끔은 서로 눈치를 보면서 장난을 멈추기도 합니다. "
            f"결국 이 조합은 중간 점수지만, 함께 있는 순간이 꽤 재미있고 즐거워요."
        ]
        return random.choice(templates_mid)
    elif score <= 99:
        templates_high = [
            f"'{w1}': '너 오늘 왜 이렇게 귀여워?' 💖\n"
            f"'{w2}': '뭐? 너도 그거 느끼고 있지?' \n"
            f"둘은 서로를 보며 장난을 치고, 동시에 서로의 마음을 읽어요. "
            f"작은 행동 하나에도 행복을 느끼고, 서로 웃음을 이끌어냅니다. "
            f"주변 사람들도 자연스럽게 둘의 케미에 빠져들고, 심장이 두근거리는 순간이 많아요."
        ]
        return random.choice(templates_high)
    else:
        templates_perfect = [
            f"'{w1}': '드디어 우리가 만났구나! 💍'\n"
            f"'{w2}': '맞아! 이제 세상 모든 폭죽은 우리를 위해 터지겠네! 🎆'\n"
            f"둘은 서로를 바라보며 천생연분임을 확신합니다. "
            f"한 발짝 다가서면 서로 손을 잡고, 웃음과 사랑이 넘쳐흐릅니다. "
            f"모든 주변이 축제처럼 변하고, 보는 사람들까지 행복하게 만드는 완벽한 조합이에요."
        ]
        return random.choice(templates_perfect)

# 점수별 색상
def get_score_style(score):
    if score <= 20: return "color:blue; background-color:#a0c4ff; padding:10px; border-radius:15px;"
    elif score <= 40: return "color:darkblue; background-color:#bdb2ff; padding:10px; border-radius:15px;"
    elif score <= 60: return "color:purple; background-color:#ffc6ff; padding:10px; border-radius:15px;"
    elif score <= 80: return "color:orange; background-color:#ffd6a5; padding:10px; border-radius:15px;"
    elif score <= 99: return "color:red; background-color:#ffadad; padding:10px; border-radius:15px;"
    else: return "color:white; background-color:#ff69b4; padding:10px; border-radius:15px; font-weight:bold;"

# 궁합 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    # 초기화
    score_placeholder.empty()
    result_placeholder.empty()
    effect_placeholder.empty()

    score = random.randint(0,100)
    score_style = get_score_style(score)
    score_placeholder.markdown(f'<div class="equals" style="{score_style}">= {score}%</div>', unsafe_allow_html=True)
    result_placeholder.markdown(f'<div class="result_text">{generate_long_funny_reason(score, w1, w2)}</div>', unsafe_allow_html=True)
    show_explosion(score)

    if score == 100:
        st.markdown("""
        <div style='text-align:center; margin-top:20px;'>
            <img src='https://i.ibb.co/2Zr91gF/bride.png' width='180'>
            <img src='https://i.ibb.co/7Yw2gFt/groom.png' width='180'>
            <p style='font-size:60px;color:red;'>💖 신랑과 신부 등장! 💖</p>
        </div>
        """, unsafe_allow_html=True)
        show_explosion(score)

# 단어 초기화
if st.button("단어 초기화 🔄"):
    st.session_state.word1 = ""
    st.session_state.word2 = ""
    score_placeholder.empty()
    result_placeholder.empty()
    effect_placeholder.empty()
