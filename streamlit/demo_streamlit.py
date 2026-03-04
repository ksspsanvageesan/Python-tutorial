import streamlit as st

st.title("Streamlit Demo")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! Welcome to Streamlit!")
    else:
        st.error("Please enter your name before submitting.")