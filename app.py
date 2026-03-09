import streamlit as st

# ------------------- Безопасный импорт -------------------
try:
    from streamlit_extras.let_it_rain import rain
    rain_available = True
except ImportError:
    rain_available = False

st.set_page_config(page_title="Поздравительный квест")

# ------------------- Цветочный дождь -------------------
if rain_available:
    import random
    for _ in range(30):
        rain(
            emoji="🌸",
            font_size=random.randint(20, 30),
            falling_speed=random.uniform(2.5, 5),
            animation_length="infinite"
        )

# ------------------- Стили -------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"] {
    font-family: 'Lobster', cursive;
}

/* градиентный фон */
body {
    background: linear-gradient(to bottom, #ffd1dc, #ff99b6) !important;
    overflow-x:hidden;
}

/* текст */
h1,h2,h3{
color:#cd7f32;
text-align:center;
}

/* блоки */
.block{
background:white;
padding:20px;
border-radius:15px;
margin-bottom:20px;
box-shadow:0 0 15px rgba(0,0,0,0.2);
}

/* поле ввода */
div.stTextInput > div > div > input{
border:1px solid green;
border-radius:6px;
}

/* шарики */
.balloon{
position:fixed;
bottom:-150px;
width:40px;
height:50px;
border-radius:50%;
animation:float 12s infinite ease-in;
opacity:0.6;
}
.balloon:after{
content:"";
position:absolute;
width:2px;
height:40px;
background:#555;
top:50px;
left:19px;
}
.balloon:nth-child(1){left:10%;background:#ff6b6b;animation-duration:10s;}
.balloon:nth-child(2){left:30%;background:#ffd93d;animation-duration:12s;}
.balloon:nth-child(3){left:50%;background:#6bcB77;animation-duration:14s;}
.balloon:nth-child(4){left:70%;background:#4d96ff;animation-duration:11s;}
.balloon:nth-child(5){left:90%;background:#ff9f1c;animation-duration:13s;}
@keyframes float{
0%{transform:translateY(0)}
100%{transform:translateY(-120vh)}
}

/* подарок с крышкой */
.gift-container{
position:relative;
width:200px;
margin:0 auto;
}
.gift-box{
background:#fff;
border-radius:10px;
width:200px;
height:100px;
position:relative;
box-shadow:0 0 15px rgba(0,0,0,0.3);
}
.gift-lid{
background:#ffd700;
width:200px;
height:30px;
border-radius:10px 10px 0 0;
position:absolute;
top:0;
left:0;
transition: transform 1s ease;
transform-origin: top center;
}
.gift-box.open .gift-lid{
transform: translateY(-80px) rotateX(-45deg);
}
/* текст внутри подарка */
.gift-content{
text-align:center;
font-size:20px;
margin-top:110px;
}
</style>
""", unsafe_allow_html=True)

# ------------------- Логика квеста -------------------
st.title("🎈Добро пожаловать в 🎈игру🎈")

questions = [
    ("Это твой вопрос и ты должна на него ответить","первый"),
    ("Кто едет","пароль"),
    ("Где рыба","всегда"),
    ("Как прыгать","нужен"),
    ("Когда быть","только"),
    ("Куда лететь","для"),
    ("За кем бежать","теста")
]

if "step" not in st.session_state:
    st.session_state.step = 0
if "gift_opened" not in st.session_state:
    st.session_state.gift_opened = False

for i,(q,answer) in enumerate(questions):
    if st.session_state.step >= i:
        st.markdown('<div class="block">', unsafe_allow_html=True)
        st.subheader(f"{i+1}. {q}")
        user = st.text_input("Введите пароль", key=f"input{i}")
        if st.button("Вперед", key=f"btn{i}"):
            if user.lower() == answer:
                st.success("Умничка!")
                if st.session_state.step == i:
                    st.session_state.step += 1
                    st.rerun()
            else:
                st.error("Неверный пароль")
        st.markdown('</div>', unsafe_allow_html=True)

# ------------------- Финальный блок -------------------
if st.session_state.step == 7:
    st.markdown("<h2 style='text-align:center'>Ты прошла все испытания!</h2>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if not st.session_state.gift_opened:
            if st.button("🎁 Открыть и забрать подарок 🎁"):
                st.session_state.gift_opened = True
                st.rerun()
    # контейнер подарка
    gift_class = "gift-box open" if st.session_state.gift_opened else "gift-box"
    st.markdown(f"""
    <div class="gift-container">
        <div class="{gift_class}">
            <div class="gift-lid"></div>
        </div>
        <div class="gift-content">
        {"Поздравляю! Твой подарок — Шкаф 🎉" if st.session_state.gift_opened else ""}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # конфетти и шары при открытии
    if st.session_state.gift_opened:
        if rain_available:
            rain(
                emoji="🎉",
                font_size=40,
                falling_speed=3,
                animation_length=2
            )
        st.balloons()
