import streamlit as st
import base64

st.title("Projects")
left_column, right_column = st.columns([1, 1])

# Encode GIF to base64
with open("images/lucy1.gif", "rb") as f:
    gif_bytes = f.read()
    encoded = base64.b64encode(gif_bytes).decode()

# HTML snippet for animated GIF
gif_html = f"""
    <img src="data:image/gif;base64,{encoded}" width="500">
"""

with left_column:
    st.markdown("----")
    st.markdown(gif_html, unsafe_allow_html=True)  # ✅ This displays animated GIF
    st.markdown("### AI Powered Portfolio with chatbot - Lucy")
    st.markdown(
        "<div style='text-align: justify'>"
        "Personal portfolio featuring Lucy, an AI-powered chatbot built with Streamlit, utilizing advanced prompt engineering techniques like few-shot training for an interactive and intelligent user experience."
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://github.com/gajmerK11/portfolio_with_chatbot'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>"
        "</a>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")

    st.image("images/micro_ecommerce.png", use_column_width=True)
    st.markdown("### Micro eCommerce")
    st.markdown(
        "<div style='text-align: justify'>"
        "Micro eCommerce with Python, Django, Serverless Postgres, Stripe, TailwindCSS and more. "
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://github.com/gajmerK11/micro_ecommerce'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>"
        "</a>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")

with right_column:
    st.markdown("----")
    st.image("images/studybud.png")
    st.markdown("### StudyBud")
    st.markdown(
        "<div style='text-align: justify'>"
        "A discord-like application with Python Django"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<div style='text-align: justify'>"
        "<br>"
        "<a href='https://github.com/gajmerK11/studybud'>"
        "<img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'>"
        "</a>"
        "</div>",
        unsafe_allow_html=True,
    )
    st.markdown("----")
