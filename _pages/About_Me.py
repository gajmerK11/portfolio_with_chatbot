import streamlit as st

# Define the left and right columns
right_column, left_column = st.columns([1, 2])
with right_column:
    st.markdown("<br>", unsafe_allow_html=True)
    st.image(r"images/profile.jpg", use_column_width=True)

with left_column:
    st.title("About Me")
   
    st.markdown(
        "<div style='text-align: justify'>"
        "Hey there! I’m Kumar Gajmer — a full-stack developer who blends logic with a bit of zen. 💻🧘 I love building clean, user-friendly apps using React, Django, Node.js, and more. Whether it’s crafting RESTful APIs or optimizing databases like MySQL and MongoDB, I enjoy turning complex problems into smooth solutions. Beyond the screen, I’m all about meditation, long bike rides, intense football matches (Barça fan for life! ⚽🔥), and getting lost in movies — from thrillers to feel-good classics. 🎬 I see programming as a spiritual art — the better you understand the problem, the closer you get to that “aha!” moment."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h3 style='color: #F39C12; font-size: 28px; font-weight: bold; margin-bottom: 20px;'>"
        "Clean code. Calm mind. Curious heart. That’s me in a snippet. 🏍️💡🎥"
        "</h3>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://www.linkedin.com/in/kumar-gajmer-04942b2a2/'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='https://github.com/gajmerK11'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
        "&nbsp;&nbsp;&nbsp;&nbsp;"
        "<a href='mailto:gajmerk9@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
        "</div>",
        unsafe_allow_html=True,
    )
