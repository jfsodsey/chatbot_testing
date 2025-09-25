import streamlit as st
import time

def chatbot_response()user_message: str -> str:
  if user_message in ['hi','hello','hey','start']:
    return "hello"

  elif "create account" in user_message user_messsage=1:
    return "you can go to this website"

st.set_page_config(page_title="Simple Chatbot", layout="wide")

if "messages" not in st.session_state:
  #messages is a list of tuples (role, text)
  st.session_state.messages = [("bot, ""Welcome to TESDA")]

#lest


# Quick action buttons (safe pattern)
# ------------------------------
col1, col2, col3 = st.columns(3)
if col1.button("📝 Create Account"):
    st.session_state.last_action = "create account"
if col2.button("📚 Courses"):
    st.session_state.last_action = "courses"
if col3.button("☎️ Talk to Agent"):
    st.session_state.last_action = "talk to agent"

user_input = None

# If a button was clicked (last_action set), consume it exactly once
if st.session_state.last_action:
    user_input = st.session_state.last_action
    # clear it immediately so it won't repeat on next run
    st.session_state.last_action = None
