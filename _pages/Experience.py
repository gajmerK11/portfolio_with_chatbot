import reveal_slides as rs

sample_markdown = r"""
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
<div style='text-align: justify'>
Python, Django, RESTful APIs
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
<div style='text-align: justify'>
JavaScript, React.js

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
<div style='text-align: justify'>
Soft skills enhancement, Leadership, Public Speaking, Collaboration, Team work, Networking
</div>
"""
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
