import streamlit as st
from starforce_logic import tap_once, get_rates

st.title("⭐ MapleStar Simulator")

# --- Starting Star Input ---
start_star = st.number_input("Starting Star (0 - 29)", min_value=0, max_value=29, value=0)

# Initialize session state
if "current_star" not in st.session_state:
    st.session_state.current_star = start_star

if "safeguard" not in st.session_state:
    st.session_state.safeguard = False

if "last_outcome" not in st.session_state:
    st.session_state.last_outcome = ""

# --- Display Current Info ---
st.subheader(f"Current Star: {st.session_state.current_star}")
st.write(f"Safeguard: **{'ON' if st.session_state.safeguard else 'OFF'}**")

# --- Display Rates ---
success, fail, boom = get_rates(st.session_state.current_star, st.session_state.safeguard)
st.write(
    f"**Rates:** Pass: `{success*100:.1f}%` | Fail: `{fail*100:.1f}%` | Boom: `{boom*100:.1f}%`"
)

# --- Layout Buttons ---
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
        st.session_state.current_star = start_star
        st.session_state.safeguard = False
        st.session_state.last_outcome = ""

# Display last outcome
if st.session_state.last_outcome:
    st.write(f"### Last Outcome: `{st.session_state.last_outcome}`")
