import streamlit as st

st.title("💼 SKILLS")

def render_image(name, path):
    return f"""
    <div style="text-align: center;">
        <img src="{path}" style="width:64px;height:64px;object-fit:contain;" />
        <div style="font-size: 12px; margin-top: 4px;">{name}</div>
    </div>
    """

# Helper function to create a section with logos
def display_skill_section(subheading, logos):
    st.subheader(subheading)
    cols = st.columns(len(logos))
    for col, (name, path) in zip(cols, logos):
        with col:
            st.image(path, caption=name, use_container_width=True)

# Example local image paths (replace with your actual image paths or URLs)
programming_languages = [
    ("Python", "images/python.png"),
    ("JavaScript", "images/javascript.png"),
]

frameworks = [
    ("Django", "images/django.png"),
    ("Node.js", "images/nodejs.png"),
    ("Express.js", "images/expressjs.png"),
    ("React.js", "images/reactjs.png"),
]

databases = [
    ("MySQL", "images/mysql.png"),
    ("MongoDB", "images/mongodb.png"),
]

tools = [
    ("Git", "images/git.png"),
    ("GitHub", "images/github.png"),
    ("Postman", "images/postman.png"),
]

# Display each skill section
display_skill_section("🧠 Programming Languages", programming_languages)
display_skill_section("🧩 Frameworks", frameworks)
display_skill_section("🗃️ Database Technologies", databases)
display_skill_section("🛠️ Version Control & Tools", tools)
