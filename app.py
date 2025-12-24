import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="Gemini Clone", page_icon="🤖")
st.title("🤖 Gemini AI Clone")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display previous messages
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Gemini:** {message}")

# User input
user_input = st.text_input("Ask me anything:")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    try:
        # Combine chat history for context
        context = ""
        for role, msg in st.session_state.chat_history:
            context += f"{role}: {msg}\n"

        response = model.generate_content(context)
        gemini_reply = response.text

        st.session_state.chat_history.append(("gemini", gemini_reply))
        st.experimental_rerun()

    except Exception as e:
        st.error(f"Error: {e}")

