import streamlit as st

st.set_page_config(page_title="Поздравительная игра")

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"]  {
    font-family: 'Lobster', cursive;
}

/* бронзовый текст */
.bronze {
    color:#cd7f32;
    font-size:22px;
}

/* блоки */
.block{
    background:white;
    padding:20px;
    border-radius:15px;
    margin-bottom:20px;
}

/* поле ввода */
input{
    border:2px solid red !important;
}

/* фон */
body{
    background:linear-gradient(120deg,#ffd1dc,#ffe4b5,#fffacd,#e0ffff);
}

/* анимированные шарики */

.balloon{
    position:fixed;
    bottom:-150px;
    width:60px;
    height:80px;
    border-radius:50%;
    opacity:0.7;
    animation:float 15s infinite;
}

@keyframes float{
    0%{
        transform:translateY(0);
    }
    100%{
        transform:translateY(-120vh);
    }
}

.balloon:nth-child(1){left:10%;background:red;animation-duration:12s;}
.balloon:nth-child(2){left:20%;background:blue;animation-duration:18s;}
.balloon:nth-child(3){left:40%;background:green;animation-duration:14s;}
.balloon:nth-child(4){left:60%;background:orange;animation-duration:16s;}
.balloon:nth-child(5){left:80%;background:purple;animation-duration:20s;}

/* подарок */

.gift{
    font-size:120px;
    text-align:center;
    animation:bounce 1.5s infinite;
}

@keyframes bounce{
    0%{transform:translateY(0)}
    50%{transform:translateY(-20px)}
    100%{transform:translateY(0)}
}

</style>

<div class="balloon"></div>
<div class="balloon"></div>
<div class="balloon"></div>
<div class="balloon"></div>
<div class="balloon"></div>

""", unsafe_allow_html=True)


st.title("Добро пожаловать в игру 🎈")

passwords = [
    "Первый",
    "пароль",
    "всегда",
    "нужен",
    "только",
    "для",
    "теста"
]

if "step" not in st.session_state:
    st.session_state.step = 1


for i in range(1,8):

    if st.session_state.step >= i:

        st.markdown('<div class="block">', unsafe_allow_html=True)

        st.markdown(
            '<p class="bronze">Это твой вопрос и ты должна на него ответить</p>',
            unsafe_allow_html=True
        )

        answer = st.text_input(
            "Введите пароль",
            key=f"input{i}",
            type="password"
        )

        if st.button("Вперед", key=f"btn{i}"):

            if answer == passwords[i-1]:

                st.success("Правильно! 🎉")

                if st.session_state.step == i:
                    st.session_state.step += 1

            else:
                st.error("Неверный пароль")

        st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.step == 8:

    st.balloons()

    st.markdown(
        '<div class="gift">🎁</div>',
        unsafe_allow_html=True
    )

    st.success("🎉 Поздравляю! Ты прошла весь квест! 🎉")
