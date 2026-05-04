import streamlit as st
import time
import random

st.set_page_config(page_title="BrainyBot Pro", layout="wide")

# 🌌 Advanced UI CSS
st.markdown("""
<style>
/* Background gradient */
body {
    background: linear-gradient(135deg, #0f172a, #020617);
    color: white;
}

/* Title */
h1, h2, h3 {
    color: #38bdf8;
}

/* Chat bubbles */
.chat {
    padding: 12px 16px;
    border-radius: 16px;
    margin: 8px 0;
    max-width: 70%;
    animation: fadeIn 0.3s ease-in-out;
}

.user {
    background: linear-gradient(135deg, #1e293b, #334155);
    margin-left: auto;
    text-align: right;
}

.bot {
    background: linear-gradient(135deg, #0ea5e9, #2563eb);
    color: white;
    margin-right: auto;
}

/* Glass sidebar */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.8);
    backdrop-filter: blur(10px);
}

/* Button glow */
button {
    border-radius: 10px !important;
    transition: 0.3s;
}
button:hover {
    box-shadow: 0 0 10px #38bdf8;
}

/* Animation */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(10px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Footer */
.footer {
    position: fixed;
    bottom: 8px;
    width: 100%;
    text-align: center;
    font-size: 14px;
    color: gray;
}
</style>
""", unsafe_allow_html=True)

# 🧠 Sidebar
st.sidebar.title("🤖 BrainyBot")
st.sidebar.markdown("### Your Smart AI Assistant ✨")

if st.sidebar.button("🆕 New Chat"):
    st.session_state.messages = []

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 Features")
st.sidebar.markdown("""
- 💬 Smart Chat  
- ⚡ Fast Replies  
- 🎨 Beautiful UI  
""")

st.sidebar.markdown("---")
st.sidebar.markdown("👩‍💻 Made by **Kalyani Pawar**")

# 💬 Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🏆 Header
st.markdown("## 👋 Hi, I'm **BrainyBot Pro**")
st.caption("Ask me about Python, AI, or anything!")

# ⚡ Quick buttons (engagement but useful)
col1, col2, col3 = st.columns(3)
if col1.button("What is Python?"):
    st.session_state.quick = "What is Python?"
if col2.button("Explain AI"):
    st.session_state.quick = "Explain AI"
if col3.button("Motivate me"):
    st.session_state.quick = "Motivate me"

# 🧠 Bot logic
def get_response(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "Hey there! 👋 I'm BrainyBot. What can I do for you?"
    elif "python" in text:
        return "Python is a powerful and easy programming language used in AI, web, and data science."
    elif "ai" in text:
        return "AI means machines that can learn, think, and solve problems like humans."
    elif "motivate" in text:
        quotes = [
            "Believe in yourself 💪",
            "Consistency beats talent 🚀",
            "You are closer than you think 🔥"
        ]
        return random.choice(quotes)
    elif "your name" in text:
        return "I'm BrainyBot Pro 🤖 created by Kalyani Pawar!"
    else:
        return "That's interesting! 🤔 Tell me more or try another question."

# 💬 Display messages
for msg in st.session_state.messages:
    role = msg["role"]
    text = msg["content"]

    if role == "user":
        st.markdown(f"<div class='chat user'>🧑 {text}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat bot'>🤖 {text}</div>", unsafe_allow_html=True)

# ⌨️ Input
user_input = st.chat_input("Type your message...")

# Handle quick buttons
if "quick" in st.session_state:
    user_input = st.session_state.quick
    del st.session_state.quick

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Typing effect
    with st.spinner("BrainyBot is thinking..."):
        time.sleep(1)

    reply = get_response(user_input)

    st.session_state.messages.append({"role": "bot", "content": reply})
    st.rerun()

# Footer
st.markdown("<div class='footer'>✨ Designed & Developed by Kalyani Pawar</div>", unsafe_allow_html=True)
