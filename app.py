import streamlit as st

st.title("Starforce Test App")

if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Tap!"):
    st.session_state.count += 1

st.write("Number of taps:", st.session_state.count)
