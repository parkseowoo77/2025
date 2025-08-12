import streamlit as st

# MBTI 데이터
mbti_data = {
    "INTJ": {
        "description": "전략가형 - 분석적이며 장기 계획에 강합니다.",
        "jobs": ["전략 컨설턴트", "데이터 과학자", "연구원", "정책 분석가", "엔지니어"],
        "image": "https://images.unsplash.com/photo-1521791136064-7986c2920216"
    },
    "ENFP": {
        "description": "활동가형 - 열정적이고 창의적이며 새로운 경험을 즐깁니다.",
        "jobs": ["마케터", "광고 기획자", "작가", "방송인", "창업가"],
        "image": "https://images.unsplash.com/photo-1517841905240-472988babdf9"
    },
    # ... 나머지 MBTI도 동일하게 추가
}

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천", page_icon="💡", layout="centered")
st.title("💡 MBTI 기반 진로 추천")
st.write("당신의 MBTI를 선택하면 어울리는 직업과 설명, 이미지를 보여드립니다.")

# 선택 박스
mbti = st.selectbox(
    "당신의 MBTI를 선택하세요:",
    options=sorted(mbti_data.keys())
)

# 무지개 글씨 CSS
rainbow_css = """
<style>
.rainbow-text {
  font-size: 28px;
  font-weight: bold;
  background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
"""

# 추천 버튼
if st.button("추천 받기"):
    data = mbti_data.get(mbti)
    if data:
        # HTML + CSS 적용
        st.markdown(rainbow_css, unsafe_allow_html=True)
        st.markdown(f"<div class='rainbow-text'>{mbti} - {data['description']}</div>", unsafe_allow_html=True)

        # 이미지
        st.image(data["image"], use_column_width=True)

        # 직업 리스트
        st.markdown("**💼 추천 직업**")
        for job in data["jobs"]:
            st.write(f"- {job}")
    else:
        st.warning("아직 데이터가 준비되지 않았어요!")
