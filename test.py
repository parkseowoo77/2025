import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(page_title="💖단어 궁합 테스트💖", layout="wide")

# CSS 스타일
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
input {font-size:50px; padding:60px; border-radius:30px; border:3px solid #fff; text-align:center; width:350px; height:180px; margin-bottom:20px;}
.plus {font-size:50px; color:white; margin:0 20px; font-weight:bold; display:flex; align-items:center; justify-content:center;}
.equals {font-size:60px; font-weight:bold; margin:20px 10px; display:inline;}
.score_text {font-size:60px; font-weight:bold; display:inline;}
.result_text {font-size:28px; margin-top:15px; line-height:1.5; text-align:center;}
.effect_item {position:fixed; font-size:50px; animation:flyRotate 5s ease forwards;}
@keyframes flyRotate {0% {opacity:1; transform:translateY(0) rotate(0deg);}100% {opacity:0; transform:translateY(-500px) rotate(720deg) scale(2);}}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="top_centered"><h1>🐱💖 단어 궁합 테스트 💖🐶</h1></div>', unsafe_allow_html=True)

# 입력창
col1, col2, col3 = st.columns([1,0.1,1])
with col1:
    w1 = st.text_input("첫 번째 단어", key="word1", max_chars=15)
with col2:
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
with col3:
    w2 = st.text_input("두 번째 단어", key="word2", max_chars=15)

# 결과 placeholder
result_placeholder = st.empty()
score_placeholder = st.empty()
effect_placeholder = st.empty()

# 점수 계산 (같은 점수 연속 방지)
last_score = None
def calc_score(word1, word2):
    global last_score
    def count_strokes(word):
        return sum([2 for _ in word])
    diff = abs(count_strokes(word1) - count_strokes(word2))
    score = max(0, 100 - diff * 5)
    # 같은 점수 연속 방지
    if last_score == score:
        while score == last_score:
            score = random.randint(0, 100)
    last_score = score
    return score

# 점수별 효과
def generate_effect_list(score):
    if score <= 20: return ["☔","🌧️","💧"]
    elif score <= 40: return ["💦","💧"]
    elif score <= 60: return ["💖","✨"]
    elif score <= 80: return ["🌈","💖","🎉"]
    elif score <= 99: return ["💖","🎆","🎇","✨"]
    else: return ["💍"]

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

# 웃긴 대화형 소설 이유
def generate_long_funny_reason(score, w1, w2):
    if score <= 40:
        return f"""
'{w1}': '어… 왜 거기 있어?' 😢
'{w2}': '나? 그냥 햇빛 좀 쬐려고…'
둘은 서로 눈치만 보고 있어요. 서로를 발견하고 깜짝 놀랐지만, 곧 '아무 일도 없었던 척' 하며 서성입니다.
가끔 서로 장난을 치려다 실패해서 어색하게 웃음을 짓고,
심지어 지나가는 사람들도 '저거 뭐야?' 하며 쳐다보죠.
"""
    elif score <= 70:
        return f"""
'{w1}': '이 장난감 내가 먼저 잡았다!' 😂
'{w2}': '어, 나도 하나 가져갈래!'
둘은 장난치며 놀다가 중간중간 서로를 놀리기도 하고, 웃음이 터지기도 합니다.
"""
    elif score <= 99:
        return f"""
'{w1}': '너 오늘 왜 이렇게 귀여워?' 💖
'{w2}': '뭐? 너도 느끼고 있지?'
둘은 서로의 작은 행동 하나하나에 행복을 느끼며 장난을 치고 웃음을 주고받아요.
"""
    else:
        return f"""
'{w1}': '드디어 우리가 만났구나! 💍'
'{w2}': '맞아! 이제 모든 폭죽은 우리를 위해 터지겠네!'
둘은 서로를 바라보며 천생연분임을 확신하고, 반지 💍 폭죽이 터집니다.
"""

# 점수별 색상
def get_score_style(score):
    if score <= 20: return "color:blue; background-color:#a0c4ff; padding:10px; border-radius:15px;"
    elif score <= 40: return "color:darkblue; background-color:#bdb2ff; padding:10px; border-radius:15px;"
    elif score <= 60: return "color:purple; background-color:#ffc6ff; padding:10px; border-radius:15px;"
    elif score <= 80: return "color:orange; background-color:#ffd6a5; padding:10px; border-radius:15px;"
    elif score <= 99: return "color:red; background-color:#ffadad; padding:10px; border-radius:15px;"
    else: return "color:white; background-color:#ff69b4; padding:10px; border-radius:15px; font-weight:bold;"

# 궁합 보기 버튼
if st.button("궁합 보기 ✨") and w1 and w2:
    score_placeholder.empty()
    result_placeholder.empty()
    effect_placeholder.empty()
    score = calc_score(w1, w2)
    score_style = get_score_style(score)
    score_placeholder.markdown(f'<div class="equals" style="{score_style}">= {score}%</div>', unsafe_allow_html=True)
    result_placeholder.markdown(f'<div class="result_text">{generate_long_funny_reason(score, w1, w2)}</div>', unsafe_allow_html=True)
    show_explosion(score)

# 단어 초기화
if st.button("단어 초기화 🔄"):
    st.session_state.word1 = ""
    st.session_state.word2 = ""
    score_placeholder.empty()
    result_placeholder.empty()
    effect_placeholder.empty()
