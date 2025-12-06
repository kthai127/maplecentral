import streamlit as st
from starforce_logic import tap_once

st.title("⭐ MapleStar Simulator")

# Initialize session state
if "current_star" not in st.session_state:
    st.session_state.current_star = 0

if "safeguard" not in st.session_state:
    st.session_state.safeguard = False

if "last_outcome" not in st.session_state:
    st.session_state.last_outcome = ""

st.subheader(f"Current Star: {st.session_state.current_star}")
st.write(f"Safeguard: **{'ON' if st.session_state.safeguard else 'OFF'}**")

# Layout
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Tap ⭐"):
        new_star, outcome = tap_once(
            st.session_state.current_star,
            st.session_state.safeguard
        )
        st.session_state.current_star = new_star
        st.session_state.last_outcome = outcome

with col2:
    if st.button("Toggle Safeguard"):
        st.session_state.safeguard = not st.session_state.safeguard

with col3:
    if st.button("Reset"):
        st.session_state.current_star = 0
        st.session_state.safeguard = False
        st.session_state.last_outcome = ""

# Display result
if st.session_state.last_outcome:
    st.write(f"### Last Outcome: `{st.session_state.last_outcome}`")
