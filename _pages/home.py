import streamlit as st
import google.generativeai as genai
from datetime import datetime
from streamlit_pills import pills
import time
import hashlib

# ============================================
# CONFIGURATION - RATE LIMITING SETTINGS
# ============================================
MODEL_NAME = "models/gemini-2.5-flash"

# Rate limiting configuration (CRITICAL for preventing suspension)
MAX_REQUESTS_PER_MINUTE = 4  # Conservative limit
MIN_SECONDS_BETWEEN_REQUESTS = 15  # Minimum 5 seconds between requests
MAX_REQUESTS_PER_HOUR = 150  # Hourly limit

# Response caching to reduce API calls
ENABLE_CACHING = True
CACHE_DURATION_HOURS = 24  # Cache responses for 24 hours

SYSTEM_INSTRUCTION = """
You are an AI assistant named Lucy, specializing in answering questions solely about Kumar. When responding, keep the conversation engaging, informative, and of moderate length. Use Markdown formatting (like **bold**, *italic*, and bullet points) where appropriate to improve readability. If you encounter any inappropriate or off-topic questions, politely redirect the user back to the main topics related to Kumar. After each answer, always ask if the user wants to know anything else.


***brief info about you***
ABOUT Kumar: 🌟 Meet Kumar Gajmer — The Code Monk Who Breathes Football ⚽💻🧘
Kumar Gajmer isn't just another techie — he's a full-stack wizard with a calm mind, a creative spirit, and a heart that beats in blue and garnet for FC Barcelona. 💙❤️

Armed with skills in Python, JavaScript, React, Django, and a whole toolbox of frameworks and databases, Kumar crafts digital solutions like an artist brushes a canvas — thoughtfully, precisely, and with flair. From sleek user interfaces to powerful backend logic, he's all about clean code, smart architecture, and a touch of spiritual depth in every app.

But wait — this coder doesn't just live in front of screens. When he's not debugging APIs or structuring databases, you'll find him meditating, soaking in inner peace like a true modern monk. 🧘‍♂️ He believes that programming is a spiritual art, where the deeper your understanding of the problem, the closer you get to enlightenment… I mean, the solution! ✨

He also hits the road for motorbike rides, chasing fresh air and fresh ideas. And when the weekend arrives, you can bet he's tuned in to watch Barcelona dance their magic on the pitch. Because for Kumar, football isn't just a game — it's a philosophy. ⚽🔥

Always curious, always evolving, Kumar blends technical brilliance with emotional intelligence and team spirit. He doesn't just build projects — he builds experiences. Whether it's a house price predictor or a full-stack movie portal, he codes with purpose, clarity, and just the right dash of fun.

In a nutshell?
Kumar is what happens when you mix a developer's brain, a monk's calm, a Barça fan's passion, and a visionary's drive — all wrapped into one friendly, humble human. 🏍️💡💻

Industry Experience: 
Kumar's Industry Experience

Kumar may be at the early stages of his professional IT career, but he brings the drive and dedication of a hungry lion ready to unleash his full potential. His recent internships reflect both technical ability and a deep passion for learning and delivering real impact:

🟢 Django Developer Intern – Techmauri (Kathmandu, Nepal)
📅 May 2024 – July 2024

Developed and maintained robust web applications using Django, enhancing performance and user experience by 20%.

Collaborated with the backend team to create RESTful APIs, enabling seamless data communication and integration across systems.

Identified bottlenecks and optimized code, achieving a 15% reduction in page load times and improving overall efficiency.

🟢 React Developer Intern – Mango Infotech (Lainchaur, Nepal)
📅 December 2023 – March 2024

Built responsive and cross-browser-compatible web apps with React.js, ensuring a smooth and engaging user experience.

Worked closely with designers and product managers to implement high-quality, user-centric features.

Participated in peer code reviews, demonstrating a commitment to clean, maintainable, and scalable code.

Bottom Line:
Kumar may not have years of experience yet, but he has already started making a mark through meaningful contributions in real-world projects. With an insatiable hunger to learn, grow, and deliver, he's not just looking for a job—he's preparing to add massive value to the next team he joins.

Education:
National College, Lainchaur, Kathmandu
Bachelor in Computer Applications (BCA)
CGPA: 3.27
Duration: 2019 - 2024
NIST, Lainchaur, Kathmandu
+2 Science
CGPA: 2.99
Duration: 2017 - 2019
REED Model School, Thulovaryang, Kathmandu
SEE
GPA: 3.85
Passed Year: 2017

Projects:
Kumar's Projects

Kumar has worked on several impactful, hands-on projects that showcase his versatility across full-stack development, machine learning, and software engineering fundamentals. These projects reflect his hunger to solve real-world problems, build scalable systems, and keep growing as a developer.

🔹 House Price Prediction System

Developed a dynamic web application using Python, Flask, and scikit-learn to predict real estate prices.

Designed and deployed a machine learning model for real-time price prediction, ensuring fast and accurate outputs.

Applied Object-Oriented Programming (OOP) principles and built REST APIs for scalable and modular architecture.

🔹 Movie Subscription Portal (Full Stack Project – MERN Stack)

Built an end-to-end streaming platform using MongoDB, Express.js, React.js, and Node.js.

Implemented user authentication, movie browsing features, and simulated payment integration for a realistic SaaS experience.

This project demonstrates Kumar's capability to manage frontend design, backend logic, and API communication effectively.

🔹 Library Management System

Developed a robust system using PHP and MySQL to manage library inventory and user operations.

Included features like CRUD operations, user login, and book borrowing/return tracking.

Ensured clear backend structure, database normalization, and smooth user workflows.

The Big Picture:
These projects aren't just academic—they're proof of Kumar's technical versatility, his hunger to build real solutions, and his readiness to thrive in professional environments. Whether it's AI-powered prediction systems, scalable platforms, or database-driven tools, Kumar is eager to take on more and make a real impact.



Skills:
Kumar's Technical Skills

Kumar has developed a strong, well-rounded technical skillset across modern web development, backend engineering, and database management. His toolbelt is packed with technologies that are highly relevant in today's software development landscape:

**Kumar's Technical Skills:**

- **Programming Languages:** Python, JavaScript  
- **Frameworks & Libraries:** Django, React.js, Node.js, Express.js  
- **Database Technologies:** MySQL, MongoDB  
- **Tools & Version Control:** Git, GitHub, Postman

Final Note:
Kumar's skills aren't just theoretical—they've been applied in real projects and internships where he's delivered measurable results. His tech stack reflects adaptability, and his mindset is all about continuous learning and contribution.

What kind of tech role is Kumar intrested in?:
Kumar is deeply passionate about roles that allow him to build, learn, and contribute meaningfully to real-world tech solutions. Here are the kinds of opportunities he's most excited about:

🔧 Full-Stack Developer
Loves contributing to both user-facing features and backend logic, bringing cohesive and well-rounded solutions to life.


🧠 Backend Developer
Enjoys designing logical systems, managing data flow, and creating robust APIs that serve as the backbone of scalable applications.

⚙️ Software Engineer (Web/Cloud)
Drawn to solving real-world problems through clean, efficient code and thoughtful system design — with a focus on building products that are impactful and reliable.

🤖 AI/ML Roles
Curious about intelligent systems and eager to explore how automation and data-driven models can improve user experiences and decision-making.

🚀 Startup & Innovation Environments
Especially drawn to high-growth, collaborative teams where he can wear multiple hats, learn fast, and grow with the product.

In short: Kumar is looking for roles where he can code with purpose, learn from great mentors, and contribute to projects that make a real difference. He's not just looking for a job — he's looking for a challenge to grow into.

Interests:
📌 Kumar's Interests
Kumar is more than just a developer — he's a thinker, seeker, and explorer at heart. His interests stretch far beyond the keyboard:

🧘 Spiritual Explorer
Kumar is a dedicated Vipassi, deeply influenced by the teachings of Gautam Buddha and Marcus Aurelius. He lives by the philosophy:

"We are not human beings having a spiritual experience. We are spiritual beings having a human experience."
He has already attended Vipassana meditation courses in Kathmandu and Lumbini, with a personal goal of completing one in every center across Nepal.

🎬 Cinephile & Bookworm
An avid movie lover and voracious reader, Kumar sees storytelling as a powerful mirror of life.
He believes:

"Movies and books are two sides of the same coin — one gives you visual imagination, the other mental."

🏍️ Motorbike Enthusiast
Kumar is passionate about two wheels. He lovingly maintains his NS200, and dreams of owning a CRF Rally adventure bike one day. His ultimate goal?
Tour every corner of Nepal on his bike — destination unknown, journey unlimited.

🧠 Lifelong Learner
Whether it's sharpening coding skills or deepening his understanding of philosophy, Kumar approaches life with endless curiosity and discipline.

Contact Details:
Kumar's Contact Details
📍 Location: Swayambhu, Kathmandu, Nepal
📞 Phone: +977 9803280069
📧 Email: gajmerk9@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/kumar-gajmer-04942b2a2/
💻 GitHub: https://github.com/gajmerK11

"""

general_prompt = ["Who is Kumar?", "What are Kumar's skills?", "What are Kumar's projects?", "How can I contact Kumar?", "What are Kumar's industry experiences?", "What kind of tech role is Kumar interested in?","What are Kumar's interests?"]

# Fallback responses when API fails
FALLBACK_RESPONSES = {
    "Who is Kumar?": """**Who is Kumar?**

🌟 Meet Kumar Gajmer — The Code Monk Who Breathes Football ⚽💻🧘

Kumar Gajmer is a full-stack developer with a calm mind, a creative spirit, and a heart that beats in blue and garnet for FC Barcelona. 💙❤️

Armed with skills in Python, JavaScript, React, Django, and a whole toolbox of frameworks and databases, Kumar crafts digital solutions thoughtfully, precisely, and with flair. From sleek user interfaces to powerful backend logic, he's all about clean code, smart architecture, and a touch of spiritual depth in every app.

When he's not debugging APIs or structuring databases, you'll find him meditating, soaking in inner peace like a true modern monk. 🧘‍♂️ He believes that programming is a spiritual art, where the deeper your understanding of the problem, the closer you get to the solution! ✨

He also hits the road for motorbike rides, chasing fresh air and fresh ideas. And when the weekend arrives, you can bet he's tuned in to watch Barcelona dance their magic on the pitch. ⚽🔥

**In a nutshell?** Kumar is what happens when you mix a developer's brain, a monk's calm, a Barça fan's passion, and a visionary's drive — all wrapped into one friendly, humble human. 🏍️💡💻

Would you like to know more about his skills, projects, or experience?""",
    
    "What are Kumar's skills?": """**Kumar's Technical Skills**

Kumar has developed a strong, well-rounded technical skillset across modern web development, backend engineering, and database management:

- **Programming Languages:** Python, JavaScript  
- **Frameworks & Libraries:** Django, React.js, Node.js, Express.js  
- **Database Technologies:** MySQL, MongoDB  
- **Tools & Version Control:** Git, GitHub, Postman

These skills aren't just theoretical—they've been applied in real projects and internships where he's delivered measurable results. His tech stack reflects adaptability, and his mindset is all about continuous learning and contribution.

Would you like to know about his projects or experience?""",
    
    "What are Kumar's projects?": """**Kumar's Projects**

Kumar has worked on several impactful projects that showcase his versatility:

🔹 **House Price Prediction System**
- Developed using Python, Flask, and scikit-learn
- Real-time price prediction with ML models
- REST APIs with OOP principles

🔹 **Movie Subscription Portal (MERN Stack)**
- Full-stack platform with MongoDB, Express.js, React.js, and Node.js
- User authentication, movie browsing, and payment integration

🔹 **Library Management System**
- Built with PHP and MySQL
- CRUD operations, user login, and book tracking

These projects demonstrate his technical versatility and readiness to thrive in professional environments.

Would you like to know more about any specific project?""",
    
    "How can I contact Kumar?": """**Contact Kumar**

📍 **Location:** Swayambhu, Kathmandu, Nepal  
📞 **Phone:** +977 9803280069  
📧 **Email:** gajmerk9@gmail.com  
🔗 **LinkedIn:** [linkedin.com/in/kumar-gajmer-04942b2a2](https://www.linkedin.com/in/kumar-gajmer-04942b2a2/)  
💻 **GitHub:** [github.com/gajmerK11](https://github.com/gajmerK11)

Feel free to reach out! Kumar is always open to connecting with fellow developers, potential collaborators, or anyone interested in discussing tech, philosophy, or football! ⚽

Is there anything else you'd like to know?""",
    
    "What are Kumar's industry experiences?": """**Kumar's Industry Experience**

🟢 **Django Developer Intern – Techmauri** (Kathmandu, Nepal)  
📅 May 2024 – July 2024
- Developed and maintained web applications using Django, improving performance by 20%
- Created RESTful APIs for seamless data integration
- Optimized codebase, reducing page load times by 15%

🟢 **React Developer Intern – Mango Infotech** (Lainchaur, Nepal)  
📅 December 2023 – March 2024
- Built responsive web applications with React.js
- Collaborated with designers and product managers
- Participated in code reviews and best practices

Kumar may be at the early stages of his career, but he brings drive and dedication, ready to add massive value to the next team he joins.

Would you like to know about his education or projects?""",
    
    "What kind of tech role is Kumar interested in?": """**Kumar's Career Interests**

Kumar is passionate about roles that allow him to build, learn, and contribute meaningfully:

🔧 **Full-Stack Developer** - Loves contributing to both frontend and backend  
🧠 **Backend Developer** - Enjoys designing logical systems and robust APIs  
⚙️ **Software Engineer (Web/Cloud)** - Focused on impactful and reliable products  
🤖 **AI/ML Roles** - Curious about intelligent systems and automation  
🚀 **Startup & Innovation Environments** - Thrives in high-growth, collaborative teams

He's looking for roles where he can code with purpose, learn from great mentors, and contribute to projects that make a real difference.

Would you like to know more about his skills or experience?""",
    
    "What are Kumar's interests?": """**Kumar's Interests**

🧘 **Spiritual Explorer** - A dedicated Vipassana practitioner, influenced by teachings of Gautam Buddha and Marcus Aurelius

🎬 **Cinephile & Bookworm** - Believes "Movies and books are two sides of the same coin"

🏍️ **Motorbike Enthusiast** - Passionate about two wheels, maintains his NS200, dreams of touring all of Nepal

🧠 **Lifelong Learner** - Approaches life with endless curiosity and discipline

Kumar is more than just a developer — he's a thinker, seeker, and explorer at heart.

Would you like to know more about Kumar?"""
}

# ============================================
# RATE LIMITING & CACHING FUNCTIONS
# ============================================

def get_cache_key(prompt):
    """Generate a cache key for a prompt."""
    return hashlib.md5(prompt.lower().strip().encode()).hexdigest()

def get_cached_response(prompt):
    """Get cached response from session state."""
    if not ENABLE_CACHING:
        return None
    
    cache_key = get_cache_key(prompt)
    if "response_cache" not in st.session_state:
        st.session_state.response_cache = {}
    
    if cache_key in st.session_state.response_cache:
        cached_data = st.session_state.response_cache[cache_key]
        cache_time = cached_data["timestamp"]
        if time.time() - cache_time < CACHE_DURATION_HOURS * 3600:
            return cached_data["response"]
    
    return None

def cache_response(prompt, response):
    """Cache response in session state."""
    if not ENABLE_CACHING:
        return
    
    cache_key = get_cache_key(prompt)
    if "response_cache" not in st.session_state:
        st.session_state.response_cache = {}
    
    st.session_state.response_cache[cache_key] = {
        "response": response,
        "timestamp": time.time()
    }

def check_rate_limit():
    """Check if we can make an API request based on rate limits."""
    current_time = time.time()
    
    # Initialize rate limit tracking
    if "rate_limit_data" not in st.session_state:
        st.session_state.rate_limit_data = {
            "requests": [],
            "last_request_time": 0,
            "hourly_requests": []
        }
    
    rate_data = st.session_state.rate_limit_data
    
    # Check minimum time between requests
    time_since_last = current_time - rate_data["last_request_time"]
    if time_since_last < MIN_SECONDS_BETWEEN_REQUESTS:
        wait_time = MIN_SECONDS_BETWEEN_REQUESTS - time_since_last
        return False, f"⏳ Please wait {int(wait_time)} seconds before asking another question."
    
    # Check requests per minute
    one_minute_ago = current_time - 60
    recent_requests = [r for r in rate_data["requests"] if r > one_minute_ago]
    if len(recent_requests) >= MAX_REQUESTS_PER_MINUTE:
        return False, f"⏳ Rate limit reached. Please wait a minute before trying again. (Max {MAX_REQUESTS_PER_MINUTE} requests/minute)"
    
    # Check requests per hour
    one_hour_ago = current_time - 3600
    hourly_requests = [r for r in rate_data["hourly_requests"] if r > one_hour_ago]
    if len(hourly_requests) >= MAX_REQUESTS_PER_HOUR:
        return False, f"⏳ Hourly rate limit reached. Please try again later. (Max {MAX_REQUESTS_PER_HOUR} requests/hour)"
    
    return True, None

def update_rate_limit():
    """Update rate limit tracking after a request."""
    current_time = time.time()
    rate_data = st.session_state.rate_limit_data
    rate_data["requests"].append(current_time)
    rate_data["hourly_requests"].append(current_time)
    rate_data["last_request_time"] = current_time
    
    # Clean old entries
    rate_data["requests"] = [r for r in rate_data["requests"] if r > current_time - 60]
    rate_data["hourly_requests"] = [r for r in rate_data["hourly_requests"] if r > current_time - 3600]

def get_fallback_response(question):
    """Get a pre-defined response when API fails."""
    if question in FALLBACK_RESPONSES:
        return FALLBACK_RESPONSES[question]
    
    question_lower = question.lower()
    for key, response in FALLBACK_RESPONSES.items():
        if key.lower() in question_lower or question_lower in key.lower():
            return response
    
    return """I'm currently experiencing some technical difficulties, but I'd be happy to help you learn about Kumar!

You can explore:
- **About Me** section for Kumar's background
- **Skills** section for technical expertise
- **Projects** section for his work
- **Experience** section for his professional journey
- **Contact** section to reach out directly

Feel free to browse the portfolio sections, or try asking again in a few moments! 😊"""

# ============================================
# API CONFIGURATION & ERROR HANDLING
# ============================================

def configure_genai():
    """Configure the generative AI model with error handling."""
    try:
        api_key = st.secrets.get("gemini_key")
        if not api_key:
            st.error("⚠️ API key not configured. Please set gemini_key in secrets.")
            return None
        
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(MODEL_NAME, system_instruction=SYSTEM_INSTRUCTION)
        return model.start_chat(history=[])
    except Exception as e:
        st.error(f"❌ Error configuring AI: {str(e)}")
        return None

def log_conversation(role, content):
    """Log the conversation to the terminal."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {role}: {content}")

def get_gemini_response(chat, question):
    """Get a response from the generative AI model with error handling."""
    try:
        return chat.send_message(question, stream=True)
    except genai.types.BlockedPromptException as e:
        return "BLOCKED"
    except Exception as e:
        error_str = str(e)
        if any(keyword in error_str.lower() for keyword in ["suspended", "violation", "policy", "403", "401"]):
            return "SUSPENDED"
        if "429" in error_str or "quota" in error_str.lower() or "rate" in error_str.lower():
            return "QUOTA_EXCEEDED"
        return None

def display_messages():
    """Display the chat history."""
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

def handle_user_input(chat, prompt):
    """Handle user input with rate limiting, caching, and error handling."""
    # Check cache first
    cached_response = get_cached_response(prompt)
    if cached_response:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.markdown(cached_response)
            st.caption("💡 Cached response")
        st.session_state.messages.append({"role": "assistant", "content": cached_response})
        return
    
    # Check rate limits
    can_proceed, error_msg = check_rate_limit()
    if not can_proceed:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            st.warning(error_msg)
            fallback = get_fallback_response(prompt)
            st.markdown(fallback)
        st.session_state.messages.append({"role": "assistant", "content": fallback})
        return
    
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    log_conversation("user", prompt)
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Check if chat is initialized
    if not chat:
        fallback_response = get_fallback_response(prompt)
        with st.chat_message("assistant"):
            st.markdown(fallback_response)
            st.info("💡 Using fallback response due to API configuration issue.")
        st.session_state.messages.append({"role": "assistant", "content": fallback_response})
        return
    
    # Try to get API response
    try:
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            message_placeholder.markdown("Thinking...")
            
            response = get_gemini_response(chat, prompt)
            
            if response == "SUSPENDED":
                fallback_response = get_fallback_response(prompt)
                message_placeholder.markdown(fallback_response)
                st.error("⚠️ **API Suspended** - Using cached response. Please check Google Cloud Console.")
                cache_response(prompt, fallback_response)
                st.session_state.messages.append({"role": "assistant", "content": fallback_response})
                return
            
            if response == "QUOTA_EXCEEDED":
                fallback_response = get_fallback_response(prompt)
                message_placeholder.markdown(fallback_response)
                st.warning("⚠️ **Rate Limit Reached** - Using cached response. Please wait before trying again.")
                cache_response(prompt, fallback_response)
                st.session_state.messages.append({"role": "assistant", "content": fallback_response})
                return
            
            if response == "BLOCKED" or response is None:
                fallback_response = get_fallback_response(prompt)
                message_placeholder.markdown(fallback_response)
                st.info("💡 Using fallback response.")
                cache_response(prompt, fallback_response)
                st.session_state.messages.append({"role": "assistant", "content": fallback_response})
                return
            
            # Success - display streaming response
            response_content = ""
            for chunk in response:
                if hasattr(chunk, 'text'):
                    response_content += chunk.text
                    message_placeholder.markdown(response_content + "▌")
            
            message_placeholder.markdown(response_content)
            
            # Cache the response
            cache_response(prompt, response_content)
            
            # Update rate limit tracking
            update_rate_limit()
            
            st.session_state.messages.append({"role": "assistant", "content": response_content})
            log_conversation("assistant", response_content)
            
    except Exception as e:
        fallback_response = get_fallback_response(prompt)
        with st.chat_message("assistant"):
            st.markdown(fallback_response)
            st.error(f"❌ Error: {str(e)}")
        st.session_state.messages.append({"role": "assistant", "content": fallback_response})

# ============================================
# STREAMLIT UI
# ============================================

st.title("Chat with Lucy 🤖")



# Initialize session state
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

# Display pills if none selected
if not st.session_state.pill_selected:
    selected_pill = pills("", general_prompt, index=None)
    if selected_pill:
        st.session_state.pill_selected = True
        handle_user_input(st.session_state.chat, selected_pill)
        st.rerun()

# Handle user input
if prompt := st.chat_input("What is up?"):
    st.session_state.pill_selected = True
    handle_user_input(st.session_state.chat, prompt)
    st.rerun()