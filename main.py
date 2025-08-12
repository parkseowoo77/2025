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
    "ESTP": {
        "description": "사업가형 - 활동적이고 즉흥적이며 상황 대처 능력이 뛰어납니다.",
        "jobs": ["영업 전문가", "기업가", "스포츠 코치", "이벤트 기획자", "경찰관"],
        "image": "https://images.unsplash.com/photo-1504386106331-3e4e71712b38"
    }
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
  text-align: center;
  background: linear-gradient(90deg, red, orange, yellow, green, blue, indigo, violet);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
</style>
"""

# 하트 애니메이션
hearts_animation = """
<script>
function createHeart() {
  const heart = document.createElement("div");
  heart.className = "heart";
  heart.style.left = Math.random() * 100 + "vw";
  heart.style.animationDuration = (Math.random() * 2 + 3) + "s";
  heart.innerText = "❤️";
  document.body.appendChild(heart);
  setTimeout(() => heart.remove(), 5000);
}
setInterval(createHeart, 300);
</script>
<style>
.heart {
  position: fixed;
  top: -2vh;
  font-size: 24px;
  animation: fall linear forwards;
  z-index: 9999;
}
@keyframes fall {
  to {
    transform: translateY(110vh);
    opacity: 0;
  }
}
</style>
"""

# 폭죽 애니메이션
fireworks_animation = """
<canvas id="fireworksCanvas" style="position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:9999;"></canvas>
<script>
const canvas = document.getElementById('fireworksCanvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

function random(min, max) { return Math.random() * (max - min) + min; }

class Particle {
    constructor(x, y, color) {
        this.x = x; this.y = y;
        this.color = color;
        this.radius = 2;
        this.alpha = 1;
        this.velocity = {
            x: random(-5, 5),
            y: random(-5, 5)
        };
    }
    draw() {
        ctx.save();
        ctx.globalAlpha = this.alpha;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.restore();
    }
    update() {
        this.x += this.velocity.x;
        this.y += this.velocity.y;
        this.alpha -= 0.02;
    }
}

let particles = [];

function createFirework(x, y) {
    const colors = ['#ff0000', '#ffff00', '#00ff00', '#00ffff', '#ff00ff', '#ffffff'];
    for (let i = 0; i < 50; i++) {
        particles.push(new Particle(x, y, colors[Math.floor(Math.random() * colors.length)]));
    }
}

function animate() {
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    particles.forEach((p, i) => {
        p.update();
        p.draw();
        if (p.alpha <= 0) particles.splice(i, 1);
    });
}

animate();

canvas.addEventListener('click', (e) => createFirework(e.clientX, e.clientY));
for (let i = 0; i < 5; i++) {
    setTimeout(() => createFirework(random(100, canvas.width-100), random(100, canvas.height-100)), i * 500);
}
</script>
"""

# 추천 버튼
if st.button("추천 받기"):
    data = mbti_data.get(mbti)
    if data:
        st.markdown(rainbow_css, unsafe_allow_html=True)
        st.markdown(f"<div class='rainbow-text'>{mbti} - {data['description']}</div>", unsafe_allow_html=True)

        st.image(data["image"], use_column_width=True)

        st.markdown("**💼 추천 직업**")
        for job in data["jobs"]:
            st.write(f"- {job}")

        st.balloons()  # 풍선
        st.markdown(hearts_animation, unsafe_allow_html=True)  # 하트
        st.markdown(fireworks_animation, unsafe_allow_html=True)  # 폭죽
    else:
        st.warning("아직 데이터가 준비되지 않았어요!")
