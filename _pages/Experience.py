import streamlit as st
import reveal_slides as rs
import base64

# Utility function to convert image to base64 string
def image_to_base64(path):
    with open(path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
        return f"data:image/png;base64,{encoded}"

# Load your images into base64
python_img = image_to_base64("images/python.png")
django_img = image_to_base64("images/django.png")
restapi_img = image_to_base64("images/restapi.png")
javascript_img = image_to_base64("images/javascript.png")
react_img = image_to_base64("images/reactjs.png")

# Custom CSS styles for professional polish
custom_css = """
<style>
.tech-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 50px;
    flex-wrap: wrap;
    margin-top: 20px;
}
.tech-item {
    text-align: center;
}
.tech-item img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
}
.tech-item img:hover {
    transform: scale(1.1);
}
.tech-label {
    margin-top: 8px;
    font-weight: bold;
}
</style>
"""

# Full markdown content
sample_markdown = f"""
# INDUSTRY EXPERIENCE
Brief overview of my experience till date.
---

## Techmauri
`Django Intern`
</br>
``May-Jul 2024``
<div style='text-align: justify'><b>
<li>Developed and maintained web applications using the Django framework during a 3-month internship at Techmauri, improving application performance and user experience by 20%.</li><br>
<li>Collaborated with the development team to design and implement RESTful APIs, supporting client requirements for data integration and enabling seamless communication between front-end and back-end systems.</li><br> 
<li>Debugged and optimized the existing Django codebase as part of ongoing project enhancements, leading to a 15% reduction in page load times and smoother functionality.</li><br>
</b></div>

Technologies Used
--
<b>Technologies Used</b><br>
{custom_css}
<div class="tech-container">
  <div class="tech-item">
    <img src="{python_img}" alt="Python">
    <div class="tech-label">Python</div>
  </div>
  <div class="tech-item">
    <img src="{django_img}" alt="Django">
    <div class="tech-label">Django</div>
  </div>
  <div class="tech-item">
    <img src="{restapi_img}" alt="RESTful APIs">
    <div class="tech-label">RESTful APIs</div>
  </div>
</div>

---

## Mango Infotech
`React Developer Intern`
</br>
`Dec-Mar 2024`
<div style='text-align: justify'><b>
<li>Built and maintained responsive web applications using React.js and other related technologies, ensuring cross browser compatibility and performance optimization.</li><br>
<li>Collaborated with designers, product managers, and developers to deliver high-quality, user-centric features.</li><br> 
<li>Participated in code reviews, shared feedback, and adhered to best practices for clean, maintainable code.</li><br> 
</b></div>

Technologies Used
--
<b>Technologies Used</b><br>
{custom_css}
<div class="tech-container">
  <div class="tech-item">
    <img src="{javascript_img}" alt="JavaScript">
    <div class="tech-label">JavaScript</div>
  </div>
  <div class="tech-item">
    <img src="{react_img}" alt="React.js">
    <div class="tech-label">React.js</div>
  </div>
</div>


"""

# Display the Reveal Slides
st.title("Experience")
currState = rs.slides(
    sample_markdown,
    theme="dracula",
    height=600,
    config={
        "transition": "slide",
        "width": 1100,
        "height": 1100,
        "center": True,
        "margin": 0.10,
        "scale_range": [0.1, 3.0],
    },
    initial_state={
        "indexf": -1,
    },
    markdown_props={"data-separator-vertical": "^--$"},
    key="foo",
)
