import streamlit as st

st.set_page_config(page_title="Поздравительный квест")

# ------------------- Стили -------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"]  {
    font-family: 'Lobster', cursive;
}

/* фон */
body{
background: linear-gradient(135deg,#ffd1dc,#d1ffd6,#d1e0ff);
overflow-x:hidden;
}

/* бронзовый текст */
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

/* цветочки */
.flower{
position:fixed;
top:-50px;
font-size:25px;
animation:fall 10s linear infinite;
}

.flower:nth-child(6){left:15%;}
.flower:nth-child(7){left:35%;}
.flower:nth-child(8){left:55%;}
.flower:nth-child(9){left:75%;}
.flower:nth-child(10){left:90%;}

@keyframes fall{
0%{transform:translateY(-50px)}
100%{transform:translateY(110vh)}
}

/* подарок */
.gift{
text-align:center;
font-size:35px;
padding:40px;
background:white;
border-radius:20px;
box-shadow:0 0 25px rgba(0,0,0,0.3);
animation:pop 1s ease;
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

<div class="flower">🌸</div>
<div class="flower">🌼</div>
<div class="flower">🌸</div>
<div class="flower">🌼</div>
<div class="flower">🌸</div>

""", unsafe_allow_html=True)

# ------------------- Логика квеста -------------------
st.title("Добро пожаловать в игру 🎈")

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

                st.success("Правильно!")

                if st.session_state.step == i:
                    st.session_state.step += 1
                    st.rerun()

            else:
                st.error("Неверный пароль")

        st.markdown('</div>', unsafe_allow_html=True)

# ------------------- Финальный блок -------------------
if st.session_state.step == 7:

    st.markdown("<h2 style='text-align:center'>Ты прошла все испытания!</h2>", unsafe_allow_html=True)

    if not st.session_state.gift_opened:

        if st.button("🎁 Открыть подарок 🎁"):

            st.session_state.gift_opened = True
            st.balloons()
            st.experimental_rerun()

    else:
        st.markdown("""
        <div class="gift">
        🎁 Поздравляю! Ты прошла квест! <br><br>
        Твой подарок — <b>Шкаф</b> 🎉
        </div>
        """, unsafe_allow_html=True)
