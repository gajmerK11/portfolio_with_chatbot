import streamlit as st

st.header(":mailbox: Get In Touch With Me!")

contact_form = """
<form action="https://formsubmit.co/ceb6869fa0e1638a7c95353fce8a7fbd" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="hidden" name="_subject" value="New message from your portfolio!">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
