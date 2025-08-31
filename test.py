import streamlit as st
import random
import time

st.set_page_config(page_title="단어 궁합 테스트", layout="wide")

# -----------------------------
# 스타일
# -----------------------------
st.markdown("""
<style>
.title {text-align: center; font-size: 50px; font-weight: bold;}
.input-box {width: 400px; height: 70px; font-size: 35px; text-align: center;}
.plus {font-size: 50px; text-align: center; margin: -20px;}
.equal {font-size: 50px; text-align: center; margin-top: 20px;}
.score {font-size: 60px; font-weight: bold; text-align: center;}
.reason {font-size: 25px; margin-top: 20px;}
.footer {font-size:18px; color:gray; text-align:center; margin-top:30px;}
.emoji-effect {text-align:center; font-size:50px; animation-duration:5s;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 표지 이미지
# -----------------------------
st.image(["https://i.imgur.com/0y0y0y0.png", "https://i.imgur.com/1y1y1y1.png"], width=150)  # 고양이, 강아지
st.markdown('<div class="title">단어 궁합 테스트</div>', unsafe_allow_html=True)

# -----------------------------
# 입력창
# -----------------------------
w1 = st.text_input("첫 번째 단어를 입력하세요", key="w1", max_chars=20)
w2 = st.text_input("두 번째 단어를 입력하세요", key="w2", max_chars=20)

# -----------------------------
# 점수 계산
# -----------------------------
last_score = None
def calculate_score(w1, w2):
    global last_score
    s = (sum([ord(c) for c in w1]) + sum([ord(c) for c in w2])) % 101
    if last_score == s:
        s = (s + random.randint(1, 10)) % 101
    last_score = s
    return s

# -----------------------------
# 대화형 소설 이유
# -----------------------------
def generate_funny_dialog_story(score, w1, w2):
    if score <= 40:
        return f"""
'{w1}': '어… 너 왜 내 앞에 있는 거야?' 😅  
'{w2}': '나? 그냥 지나가다가… 어, 너도 여기 있었네?'  
{w1}가 발을 헛디뎌 거의 넘어질 뻔 하고, {w2}는 놀라서 '어머! 조심해!'  
서로 눈치만 보고 한 마디도 못 하고 있음.  
길을 지나던 고양이와 강아지까지 와서 상황을 더 웃기게 만듬.  
결국 점수가 낮은 이유는, 둘의 만남이 너무 어색하고 티격태격해서 웃음을 터뜨렸기 때문입니다.
"""
    elif score <= 70:
        return f"""
'{w1}': '이거 내가 먼저 잡은 거야!' 😆  
'{w2}': '헉, 나도 가져가야지!'  
둘이 장난치며 서로의 손을 잡으려 하지만 계속 밀리고 당기고 난리남.  
점수가 중간인 이유는, 장난과 친근함이 섞여 케미가 조금 보였기 때문입니다.
"""
    elif score <= 99:
        return f"""
'{w1}': '오늘 너 완전 귀엽다!' 💖  
'{w2}': '뭐? 너도 느끼고 있잖아!'  
둘이 장난치며 길을 걷다가 {w1}가 미끄러지자 {w2}가 잡아주며 웃음 폭발.  
점수가 높은 이유는, 설렘과 웃음이 폭발하며 서로 케미가 극대화되었기 때문입니다.
"""
    else:
        return f"""
'{w1}': '드디어 우리가 만났구나! 💍'  
'{w2}': '맞아! 이제 모든 폭죽은 우리를 위해 터지겠네!'  
하늘에는 반지 💍 폭죽이 터지고, 하트와 별들이 흩날리며 완전히 황홀한 장면이 펼쳐집니다.  
점수 100%, 완전 웃기고 달콤한 궁합입니다!
"""

# -----------------------------
# 점수 출력 및 효과
# -----------------------------
if w1 and w2:
    score = calculate_score(w1, w2)
    
    st.markdown('<div class="plus">+</div>', unsafe_allow_html=True)
    st.markdown('<div class="equal">=</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="score">{score}점</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="reason">{generate_funny_dialog_story(score, w1, w2)}</div>', unsafe_allow_html=True)

    # -----------------------------
    # 점수별 화면 효과 (간단하게 반복 출력)
    # -----------------------------
    emoji = "🌧️" if score <= 40 else "✨" if score <= 70 else "💖" if score <= 99 else "💍"
    for _ in range(5):  # 5초 정도 유지
        st.markdown(f'<div class="emoji-effect">{emoji*5}</div>', unsafe_allow_html=True)
        time.sleep(1)

    # -----------------------------
    # 점수 계산 공식 & 주의사항
    # -----------------------------
    st.markdown('<div class="footer">점수 계산 공식: (단어1의 문자 합 + 단어2의 문자 합) % 101<br>※ 단순히 재미용이며 과몰입 금지!</div>', unsafe_allow_html=True)
