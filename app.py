import streamlit as st
from streamlit_extras.let_it_rain import rain as st_rain

st.set_page_config(page_title="Поздравительный квест")

# ------------------- Стили -------------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"]  {
    font-family: 'Lobster', cursive;
}

body{
background: linear-gradient(135deg,#ffd1dc,#d1ffd6,#d1e0ff);
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

/* подарок */

.gift{
text-align:center;
font-size:35px;
padding:40px;
background:white;
border-radius:20px;
box-shadow:0 0 25px rgba(0,0,0,0.3);
animation:pop 2s ease;
}

@keyframes pop{
0%{transform:scale(0)}
100%{transform:scale(1)}
}

</style>

<div class="balloon"></div>
<div class="balloon"></div>
<div class="balloon"></div>
<div class="balloon"></div>
<div class="balloon"></div>

""", unsafe_allow_html=True)

# ------------------- Цветочный дождь -------------------

rain(
    emoji="🌸",
    font_size=28,
    falling_speed=5,
    animation_length="infinite"
)

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

# ------------------- Финал -------------------

if st.session_state.step == 7:

    st.markdown("<h2 style='text-align:center'>Ты прошла все испытания!</h2>", unsafe_allow_html=True)

    if not st.session_state.gift_opened:

        if st.button("🎁 Открыть и забрать подарок 🎁"):
            st.session_state.gift_opened = True
            st.rerun()

    if st.session_state.gift_opened:

        # конфетти
        rain(
            emoji="🎉",
            font_size=40,
            falling_speed=3,
            animation_length=2
        )

        st.balloons()

        st.markdown("""
        <div class="gift">
        🎁 Поздравляю! Ты прошла квест! <br><br>
        Твой подарок — <b>Шкаф</b> 🎉
        </div>
        """, unsafe_allow_html=True)
