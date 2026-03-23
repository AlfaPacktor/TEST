import streamlit as st
import random

st.set_page_config(page_title="Поздравительный квест")

# ------------------- Стили -------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"]  {
    font-family: 'Lobster', cursive;
}

/* фон */
.stApp {
background: linear-gradient(135deg,#ffd1dc,#d1ffd6,#d1e0ff);
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

.balloon:nth-child(1){left:0%;background:#ff6b6b;animation-duration:5s;}
.balloon:nth-child(2){left:90%;background:#ff9f1c;animation-duration:13s;}
.balloon:nth-child(3){left:10%;background:#ff6b6b;animation-duration:10s;}
.balloon:nth-child(4){left:30%;background:#ffd93d;animation-duration:12s;}
.balloon:nth-child(5){left:50%;background:#6bcB77;animation-duration:14s;}

@keyframes float{
0%{transform:translateY(0)}
100%{transform:translateY(-120vh)}
}

/* цветочки */
.flower{
position:fixed;
top:-50px;
font-size:25px;
animation:fall linear infinite;
}

@keyframes fall{
0%{transform:translateY(-50px)}
100%{transform:translateY(110vh)}
}

/* сердечки */
.heart{
position:fixed;
top:-50px;
animation:fallHeart linear infinite;
opacity:0.8;
z-index:999;
}

@keyframes fallHeart{
0%{
transform:translateY(-50px) translateX(0px) rotate(0deg);
}
50%{
transform:translateY(50vh) translateX(30px) rotate(180deg);
}
100%{
transform:translateY(110vh) translateX(-30px) rotate(360deg);
}
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

# ------------------- Сердечки -------------------
hearts_html = ""
for i in range(20):
    left = random.randint(0, 100)
    duration = random.randint(8, 15)
    delay = random.randint(0, 10)
    size = random.randint(16, 30)

    hearts_html += f'''
    <div class="heart"
         style="
         left:{left}%;
         font-size:{size}px;
         animation-duration:{duration}s;
         animation-delay:{delay}s;">
         ❤️
    </div>
    '''

st.markdown(hearts_html, unsafe_allow_html=True)


st.markdown(hearts_html, unsafe_allow_html=True)

# ------------------- Цветочки -------------------
flowers_html = ""
for i in range(10):
    left = random.randint(0, 100)
    duration = random.randint(10, 20)
    delay = random.randint(0, 10)

    flowers_html += f'''
    <div class="flower"
         style="
         left:{left}%;
         animation-duration:{duration}s;
         animation-delay:{delay}s;">
         🌸
    </div>
    '''

st.markdown(flowers_html, unsafe_allow_html=True)

# ------------------- Логика квеста -------------------
st.title("🎈Добро🌼 пожаловать в 🎈игру🎈")

questions = [
("Это твой первый вопрос и ты должна на него ответить 'правильно'","правильно"),
("Молодец! Теперь скажи, как звали нашего итальянского четверолапого гангстера Азоффа?","донни"),
("Супер! А что значит Б. Восток?","большой"),
("Умничка! Как называется самая большая статуя на Бали?","гаруда вишну"),
("Молодец! Если у меня спросят, сколько лет мы вместе, то как я отвечу?","10 лет"),
("Заюшка, как называлась та белая машина в наш день?","мустанг"),
("Умничка! Теперь спроси у робота Где товар?","верх")
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

            if user.strip().lower() == answer.strip().lower():

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

    if not st.session_state.get("gift_opened", False):

        if st.button("🎁🎁🎁 Открыть и забрать подарок 🎁🎁🎁"):
            st.session_state.gift_opened = True

    if st.session_state.get("gift_opened", False):
        st.balloons()
        st.markdown("""
        <div class="gift">
        🎁 Поздравляю! Ты прошла квест! <br><br>
        Твоя подсказка — <b>Комод CaRL</b> 🎉
        </div>
        """, unsafe_allow_html=True)
