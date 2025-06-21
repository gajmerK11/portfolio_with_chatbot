import streamlit as st
from PIL import Image

def combine_images(image_paths, image_size=(100, 100), gap=20):
    images = [Image.open(path).resize(image_size) for path in image_paths]

    total_width = sum(img.width for img in images) + gap * (len(images) - 1)
    max_height = max(img.height for img in images)

    combined = Image.new('RGBA', (total_width, max_height), (255, 255, 255, 0))

    x_offset = 0
    for img in images:
        combined.paste(img, (x_offset, 0))
        x_offset += img.width + gap

    return combined

# ------------------------
# SKILLS DATA
# ------------------------

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

# ------------------------
# DISPLAY FUNCTION
# ------------------------

def display_skill_section(title, logos):
    st.subheader(title)
    image_paths = [path for name, path in logos]
    combined = combine_images(image_paths, gap=20)
    st.image(combined)

# ------------------------
# RENDER ALL SECTIONS
# ------------------------

st.title("💼 SKILLS")

display_skill_section("🧠 Programming Languages", programming_languages)
display_skill_section("🧩 Frameworks", frameworks)
display_skill_section("🗃️ Database Technologies", databases)
display_skill_section("🛠️ Version Control & Tools", tools)
