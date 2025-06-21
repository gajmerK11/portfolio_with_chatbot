import streamlit as st
import base64
from pathlib import Path

# Path to the PDF file
pdf_file_path = "assets/resume.pdf"

def display_pdf(file_path):
    with open(file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000px" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

def download_button(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    st.download_button(label="📄 Download Resume PDF", data=data, file_name="Kumar_Resume.pdf", mime="application/pdf")

def main():
    st.title("Resume")

    st.write("Click the button to download a full copy of the resume.")
    download_button(pdf_file_path)

    st.markdown("---")
    display_pdf(pdf_file_path)

if __name__ == "__main__":
    main()
