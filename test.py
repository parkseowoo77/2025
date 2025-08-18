import streamlit as st
import random

st.set_page_config(page_title="단어 궁합 앱 💖", layout="centered")

st.title("💖 좋아하는 단어 궁합 앱 💖")
st.write("각자 좋아하는 단어를 입력하면 궁합 점수를 확인해보세요!")

# 캐릭터 이미지 URL
kitty_url = "https://upload.wikimedia.org/wikipedia/en/0/0b/Hello_Kitty.svg"
mymelody_url = "https://upload.wikimedia.org/wikipedia/en/f/f1/My_Melody.svg"
kuromi_url = "https://upload.wikimedia.org/wikipedia/en/0/0c/Kuromi.svg"

st.image([kitty_url, mymelody_url, kuromi_url], width=100, caption=["헬로키티", "마이멜로디", "쿠로미"])

# 사용자 입력
word1 = st.text_input("첫 번째 사람의 좋아하는 단어")
word2 = st.text_input("두 번째 사람의 좋아하는 단어")

if st.button("궁합 보기"):
    if word1 and word2:
        # 점수 계산
        length_score = max(0, 10 - abs(len(word1) - len(word2)))
        common_letters = len(set(word1) & set(word2))
        random_score = random.randint(0, 10)
        total_score = length_score + common_letters + random_score
        total_score = min(total_score, 30)

        # 점수별 효과
        if total_score > 25:
            st.balloons()  # 풍선/하트 폭죽
            st.markdown('<h3 style="color:#ff1493">🎉 완전 찰떡 궁합! 🎉</h3>', unsafe_allow_html=True)
            st.write("👏 박수와 함께 축하해요! 너무 잘 맞아요! 😍")
        elif total_score > 18:
            st.markdown('<h3 style="color:#ff69b4">💕 서로 잘 맞는 편이에요! 💕</h3>', unsafe_allow_html=True)
            st.write("🎈 귀여운 하트와 풍선이 터졌어요! 😊")
        else:
            st.markdown('<h3 style="color:#1e90ff">☔ 조금 아쉬운 궁합이에요 ☔</h3>', unsafe_allow_html=True)
            st.write("💧 비가 내리는 분위기지만, 노력하면 좋아질 수 있어요! 😉")
            # 비 내리는 효과: CSS 애니메이션으로 간단히 표현
            st.markdown(
                """
                <style>
                @keyframes rain {
                    0% {top: -10px;}
                    100% {top: 100%;}
                }
                .drop {
                    position: absolute;
                    width: 2px;
                    height: 10px;
                    background: #1e90ff;
                    animation: rain 1s linear infinite;
                }
                </style>
                <div class="drop"></div>
                <div class="drop" style="left: 30px; animation-delay: 0.3s;"></div>
                <div class="drop" style="left: 60px; animation-delay: 0.6s;"></div>
                """, unsafe_allow_html=True
            )

        st.markdown(f"<p style='font-size:20px'>💌 {word1} 💕 {word2} 점수: {total_score}/30</p>", unsafe_allow_html=True)
    else:
        st.warning("두 사람의 단어를 모두 입력해주세요! 📝")

