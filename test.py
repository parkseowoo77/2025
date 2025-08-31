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
    score = random.randint(0, 100)
    while last_score is not None and score == last_score:
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

# 길게 설명된 이유
def generate_long_funny_reason(score, w1, w2):
    if score <= 40:
        return f"""
'{w1}'와 '{w2}'는 서로 눈치를 보며 어색하게 마주칩니다.  
처음에는 장난을 치고 싶어도 상대가 어떻게 반응할지 몰라서 주춤거리고,  
서로 말 한마디도 조심스러워하며, 때때로 지나가는 사람의 시선 때문에 멈칫합니다.  
하지만 이런 소심함과 어색함 속에서도 서로를 살짝 바라보고,  
작은 미소를 주고받는 순간들이 있습니다.  
결국 점수가 낮게 나온 이유는 서로가 너무 조심스럽고 수줍어해서,  
조금은 귀엽지만 장난기 넘치진 못하는 상황 때문이에요.
"""
    elif score <= 70:
        return f"""
'{w1}'와 '{w2}'는 장난을 치며 서로에게 웃음을 주고받는 즐거운 상황이 이어집니다.  
때로는 서로 장난이 과열되어 뒤엉키기도 하고,  
주변 사람들도 '두 사람 정말 장난꾸러기네!'라고 감탄할 정도입니다.  
서로의 작은 장난에 웃음이 터지기도 하고,  
가끔은 장난이 실패해 어색하게 웃음을 지어야 할 때도 있어요.  
이런 여러 상황들이 모여서 점수가 중간 정도로 나온 것입니다.  
즉, 장난기와 귀여움이 섞여서 알맞은 케미를 보여주는 구간이에요.
"""
    elif score <= 99:
        return f"""
'{w1}'와 '{w2}'는 서로의 귀여움과 장난에 행복을 느끼며,  
서로를 바라보는 순간마다 작은 설렘과 즐거움을 공유합니다.  
서로가 한 행동 하나하나에 관심을 기울이고, 장난을 치며 웃음을 주고받습니다.  
때때로 주변 사람들도 이 케미를 느끼며 흐뭇하게 바라보죠.  
이들은 서로에게 긍정적인 에너지를 주며, 장난과 웃음 속에서 깊은 유대감을 형성합니다.  
이런 이유로 점수가 높게 나온 것입니다.  
서로의 장난과 귀여움이 잘 맞아, 함께 있을 때 분위기가 밝고 즐거워요.
"""
    else:
        return f"""
'{w1}'와 '{w2}'는 완벽한 궁합을 보여줍니다. 💖  
처음 만났을 때부터 서로의 눈빛과 행동에서 자연스럽게 마음이 통하고,  
작은 장난 하나에도 웃음이 터지고 서로에게 즐거움을 선사합니다.  
주변에 폭죽과 같은 즐거움이 퍼지듯, 그들의 케미와 행복은 눈에 보이는 듯합니다.  
둘은 서로를 바라보며 미래의 모험과 즐거움을 상상하고,  
장난과 웃음 속에서도 서로에게 힘과 위안을 주는 관계를 만들어 갑니다.  
점수 100%는 이러한 완벽한 조화와 긍정적인 에너지를 상징하며,  
모든 것이 축제처럼 느껴지는 천생연분임을 보여줍니다.
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

# 주의사항만 표시
st.markdown("""
<hr style='border:2px dashed white;'/>
<div style='text-align:center; color:white; font-size:20px; margin-top:20px;'>
<b>⚠️ 주의사항:</b> 단순 재미용입니다. 과몰입 금지! 😆
</div>
""", unsafe_allow_html=True)
