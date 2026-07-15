import streamlit as st
from llm_engine import get_stadium_assistance

# Page configurations for a clean, accessible look
st.set_page_config(
    page_title="StadiumBuddy AI", 
    page_icon="⚽", 
    layout="centered"
)

# Title & App Branding
st.title("⚽ StadiumBuddy AI")
st.subheader("World Cup 2026 Smart Stadium & Operations Hub")
st.write(
    "Real-time crowd routing, multilingual support, and hyper-accessible stadium assistance."
)

st.divider()

# Setup Columns for configurations
col1, col2 = st.columns(2)

with col1:
    role = st.selectbox(
        "Who are you?",
        ["Fan / Spectator", "Stadium Volunteer", "Security & Operations Staff"]
    )

with col2:
    language = st.selectbox(
        "Choose Language / Idioma / Langue",
        ["English", "Español", "Français", "Deutsch", "Português"]
    )

st.divider()

# Input box with an accessibility-friendly label
user_query = st.text_area(
    "Ask anything about stadium layout, crowds, or transport:",
    placeholder="e.g., How do I guide a fan in a wheelchair from Gate 3 to the accessible seating area?"
)

# Submit button
if st.button("Get AI Guidance", use_container_width=True):
    if user_query.strip() == "":
        st.warning("Please type a question or scenario first!")
    else:
        with st.spinner("Analyzing stadium operations and generating paths..."):
            try:
                ai_response = get_stadium_assistance(user_query, language, role)
                st.success("🤖 Operations Desk Response:")
                st.info(ai_response)
            except Exception as e:
                st.error(f"Something went wrong: {e}")