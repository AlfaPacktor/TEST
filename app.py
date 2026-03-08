import streamlit as st

st.set_page_config(page_title="Поздравительная игра")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Lobster&display=swap');

html, body, [class*="css"]  {
    font-family: 'Lobster', cursive;
}

.block {
    border-radius:15px;
    padding:20px;
    margin-bottom:20px;
    background:white;
}

input {
    border:2px solid red !important;
}

.bronze {
    color:#cd7f32;
    font-size:22px;
}
</style>
""", unsafe_allow_html=True)


st.title("Добро пожаловать в игру 🎈")


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

            if answer == str(i):

                st.success("Правильно! 🎉")

                if st.session_state.step == i:
                    st.session_state.step += 1

            else:
                st.error("Неверный пароль")

        st.markdown('</div>', unsafe_allow_html=True)


if st.session_state.step == 8:
    st.balloons()
    st.success("🎉 Поздравляю! Ты прошла весь квест! 🎉")
