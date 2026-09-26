
import streamlit as st

st.title("My First Streamlit App")
st.write("A simple live application deployed from GitHub.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! 👋")
    else:
        st.warning("Please enter your name.")
