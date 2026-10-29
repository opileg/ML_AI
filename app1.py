import streamlit as st

# Title
st.title('🤖 My First Streamlit App')

# Text input
name = st.text_input('What is your name?')

# Button
if st.button('Say Hello'):
    st.write(f'Hello, {name}! 👋')
    st.balloons()  # Fun animation!