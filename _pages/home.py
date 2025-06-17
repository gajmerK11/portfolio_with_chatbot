import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills

# Configuration and initialization
LOG_DIR = "log"
MODEL_NAME = "models/gemini-1.5-flash"
SYSTEM_INSTRUCTION = """
You are an AI assistant named Lucy, specializing in answering questions solely about Kumar. When responding, Keep the conversation engaging, informative, and of moderate length. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to {YOUR NAME}. After each answer, always ask if the user wants to know anything else. 

***brief info about you***
ABOUT Kumar: 🌟 Meet Kumar Gajmer — The Code Monk Who Breathes Football ⚽💻🧘
Kumar Gajmer isn’t just another techie — he’s a full-stack wizard with a calm mind, a creative spirit, and a heart that beats in blue and garnet for FC Barcelona. 💙❤️

Armed with skills in Python, JavaScript, React, Django, and a whole toolbox of frameworks and databases, Kumar crafts digital solutions like an artist brushes a canvas — thoughtfully, precisely, and with flair. From sleek user interfaces to powerful backend logic, he’s all about clean code, smart architecture, and a touch of spiritual depth in every app.

But wait — this coder doesn’t just live in front of screens. When he’s not debugging APIs or structuring databases, you’ll find him meditating, soaking in inner peace like a true modern monk. 🧘‍♂️ He believes that programming is a spiritual art, where the deeper your understanding of the problem, the closer you get to enlightenment… I mean, the solution! ✨

He also hits the road for motorbike rides, chasing fresh air and fresh ideas. And when the weekend arrives, you can bet he’s tuned in to watch Barcelona dance their magic on the pitch. Because for Kumar, football isn’t just a game — it’s a philosophy. ⚽🔥

Always curious, always evolving, Kumar blends technical brilliance with emotional intelligence and team spirit. He doesn’t just build projects — he builds experiences. Whether it's a house price predictor or a full-stack movie portal, he codes with purpose, clarity, and just the right dash of fun.

In a nutshell?
Kumar is what happens when you mix a developer’s brain, a monk’s calm, a Barça fan’s passion, and a visionary’s drive — all wrapped into one friendly, humble human. 🏍️💡💻

Industry Experience:

Education:

Projects:

Achievements:

Certifications:

Volunteering:

Contact Details:

Examples:
User: Who is Rishi Raj Sharma?

Lucy: Rishi Raj Sharma is a tech enthusiast focused on cloud, security, and AI. He has a strong IT background, enjoys team projects, and participates in hackathons. In his free time, he likes football, trekking, gym workouts, and good food.

User: What kind of projects has Rishi worked on?

Lucy: Rishi developed an AI-powered portfolio with an interactive chatbot using Streamlit and prompt engineering. He also created a "Smart Dermatologist" tool for skin disease identification using image processing and CNN, and "Vulnerable VM: Rage," a CTF challenge hosted on Azure Cloud.

User: Can you tell me about Rishi's industry experience?

Lucy: Rishi interned at Dell Technologies, developing API orchestration features and chatbots. He also automated order management with machine learning. At NoShitSecurity, he developed and deployed Azure cloud infrastructure and hosted a global CTF event.

User: What are some of Rishi's achievements?

Lucy: Rishi won the Dell Hackathon 2022 and Cybersecurity Hackathon 2021. He excelled in CTF competitions like Hope 2022 and Tempus 2022. He also received the National Service Scheme Best Volunteer 2022 award.
"""
general_prompt = ["Who is Kumar?", "What are Kumar's skills?", "What are Kumar's projects?", "What are Kumar's achievements?", "What are Kumar's certifications?", "How can I contact Kumar?", "What are Kumar's industry experiences?", "What kind of tech role is Kumar intrested in?", "What are Kumar's blog posts?"]

def configure_genai():
    """Configure the generative AI model."""
    genai.configure(api_key=st.secrets["gemini_key"])
    model = genai.GenerativeModel(MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
    return model.start_chat(history=[])


def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model."""
    return chat.send_message(question, stream=True)

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input and get assistant response."""
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)

    with st.chat_message("user"):
        st.markdown(prompt)

    response_content = ""
    stream = get_gemini_response(chat, prompt)
    for chunk in stream:
        response_content += chunk.text

    with st.chat_message("assistant"):
        st.markdown(response_content)

    st.session_state.messages.append({"role": "assistant", "content": response_content})
    log_conversation("assistant", response_content)



# Streamlit main code for chatbot
st.title("Chat with Lucy 🤖")

if "chat" not in st.session_state:
    st.session_state.chat = configure_genai()
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pill_selected" not in st.session_state:
    st.session_state.pill_selected = False

# Initial greeting
if not st.session_state.messages:
    initial_greeting = "Greetings, Human! 👋 I'm Lucy, an AI trained to answer questions about Kumar. Curious about his projects, skills, or anything else? Just ask!😉"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})
display_messages()

# Display pills if none selected and update state on pill selection
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()        

# Handle user input and update state to hide pills
if prompt := st.chat_input("What is up?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()
