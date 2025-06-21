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

# Build your full markdown content with embedded images
sample_markdown = f"""
# INDUSTRY EXPERIENCE
Brief overview of my experience till date.
---

## Techmauri
`Django Intern`
</br>
``May-Jul 2024``
<div style='text-align: justify'><b>
<li>
Developed and maintained web applications using the Django framework during a 3-month internship at Techmauri, improving application performance and user experience by 20%.</li><br>

<li> Collaborated with the development team to design and implement RESTful APIs, supporting client requirements for data integration and enabling seamless communication between front-end and back-end systems.</li><br> 

<li>Debugged and optimized the existing Django codebase as part of ongoing project enhancements, leading to a 15% reduction in page load times and smoother functionality.</li><br>
</b>
</div>

Technologies Used
--
<b>Technologies Used</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style="display: flex; justify-content: center; align-items: center; gap: 40px;">
  <div style="text-align: center;">
    <img src="{python_img}" alt="Python" style="width:80px;"><br>Python
  </div>
  <div style="text-align: center;">
    <img src="{django_img}" alt="Django" style="width:80px;"><br>Django
  </div>
  <div style="text-align: center;">
    <img src="{restapi_img}" alt="RESTful APIs" style="width:80px;"><br>RESTful APIs
  </div>
</div>

---

## Mango Infotech
`React Developer Intern`
</br>
`Dec-Mar 2024`
<div style='text-align: justify'><b>
<li> Built and maintained responsive web applications using React.js and other related technologies, ensuring cross browser compatibility and performance optimization.</li><br>

<li>Collaborated with designers, product managers, and developers to deliver high-quality, user-centric features.</li><br> 

<li> Participated in code reviews, shared feedback, and adhered to best practices for clean, maintainable code.</li><br> 
</b>
</div>

Technologies Used
--
<b>Technologies Used</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style="display: flex; justify-content: center; align-items: center; gap: 40px;">
  <div style="text-align: center;">
    <img src="{javascript_img}" alt="JavaScript" style="width:80px;"><br>JavaScript
  </div>
  <div style="text-align: center;">
    <img src="{react_img}" alt="React.js" style="width:80px;"><br>React.js
  </div>
</div>

---

## Nobel Learning PBC
`Intern`
</br>
`May-Present (Remote) 2025`
<div style='text-align: justify'><b>
<li>Participating in a structured program focused on enhancing soft skills essential for a professional IT environment.</li><br>

<li> Developing leadership qualities by taking initiative in group tasks and leading small project components.</li><br> 
</b>
</div>

Skills Learned
--
<b>Skills Learned</b><br>
<!-- .slide: data-background-color="#283747" -->
<div style="text-align: justify;">
Soft skills enhancement, Leadership, Public Speaking, Collaboration, Team work, Networking
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
