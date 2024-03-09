import streamlit as st

st.set_page_config(
    page_title="Form",
    page_icon="👋",
)

st.title("Welcome to Stream-bot, a Student and Career Advisor Chatbot.")

#st.sidebar.header("Form")

title = st.text_input('Favourite courses')
title = st.text_input('Do you like working independently or with company?')
title = st.text_input('long term career goals')
title = st.text_input('what inspires you')
title = st.text_input('skills and talents')

st.button('Submit')