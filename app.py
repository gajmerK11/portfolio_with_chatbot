import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Kumar's Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="auto",
)
with st.sidebar:
    choose = option_menu(
        "Kumar Gajmer",
        [
            "Lucy",
            "About Me",
            "Experience",
            "Skills",
            "Education",
            "Projects",
            "Resume",
            "Contact",
        ],
        icons=[
            "robot",
            "person fill",
            "clock history",
            "tools",
            "book half",
            "clipboard",
            "file-earmark-person",
            "envelope",
        ],
        menu_icon="mortarboard",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#0D1117"},
            "icon": {"color": "darkorange", "font-size": "20px"},
            "nav-link": {
                "font-size": "17px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#1F2937",
            },
            "nav-link-selected": {"background-color": "#A41117"},
        },
    )
    st.markdown(
    "<div style='text-align: center;'>"
    "<a href='https://www.linkedin.com/in/kumar-gajmer-04942b2a2/'><img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='40'></a>"
    "&nbsp;&nbsp;&nbsp;&nbsp;"
    "<a href='https://github.com/gajmerK11'><img src='https://upload.wikimedia.org/wikipedia/commons/2/24/Github_logo_svg.svg' width='40'></a>"
    "&nbsp;&nbsp;&nbsp;&nbsp;"
    "<a href='mailto:gajmerk9@gmail.com'><img src='https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png' width='40'></a>"
    "</div>",
    unsafe_allow_html=True,
)

pages = {
    "Lucy": "_pages/home.py",
    "About Me": "_pages/About_Me.py",
    "Experience": "_pages/Experience.py",
    "Skills": "_pages/Skills.py",
    "Education": "_pages/Education.py",
    "Projects": "_pages/Projects.py",
    "Contact": "_pages/Contact.py",
}

# Dynamically load the selected page
page_file = pages.get(choose)
if page_file:
    with open(page_file, encoding="utf-8") as file:
        exec(file.read())

elif choose == "Resume":
    import base64
    from pathlib import Path

    st.title("Resume")
    # st.write("Click the button to download a full copy of the resume.")

    resume_path = "assets/resume.pdf"

    with open(resume_path, "rb") as f:
        resume_data = f.read()

    st.download_button(
        label="📄 Download Resume PDF",
        data=resume_data,
        file_name="Kumar_Gajmer_Resume.pdf",
        mime="application/pdf"
    )

    # # Display the embedded PDF
    # base64_pdf = base64.b64encode(resume_data).decode("utf-8")
    # pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000px" type="application/pdf"></iframe>'
    # st.markdown("---")
    # st.markdown(pdf_display, unsafe_allow_html=True)

