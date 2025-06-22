# 💼 Kumar Gajmer – Portfolio Website

Welcome to my personal portfolio website, developed using Python with Streamlit to create a seamless, data-driven web interface and integrated with an AI-powered assistant. This site highlights my professional background, technical skills, and projects — with a conversational chatbot to answer your questions interactively.

🌐 **Live Demo**: https://kumar-gajmer.onrender.com
📂 **Project Folder**: `portfolio_with_chatbot/`

---

## 🚀 Features

### 🧠 Lucy – The AI Assistant

> A GPT-powered chatbot integrated into the portfolio. It can answer questions about me, guide users through the site, and showcase natural language capabilities.

- Powered by `google-generativeai` (Gemini API)
- Integrated into the Streamlit sidebar
- Real-time chat experience with a personalized tone

### 🖥️ Streamlit Web Interface

- **Modern UI** with `streamlit_option_menu` and `streamlit_pills`
- Fully responsive layout (`wide` mode)
- Modular design with sections: About Me, Skills, Projects, Education, Resume

---

## 🛠️ Tech Stack

| Tool/Library              | Purpose                                            |
| ------------------------- | -------------------------------------------------- |
| `Streamlit`               | Core web app framework                             |
| `google-generativeai`     | Integrates Gemini LLM for chatbot                  |
| `streamlit_option_menu`   | Sidebar navigation UI                              |
| `streamlit_pills`         | Tab-like navigation pills                          |
| `streamlit_reveal_slides` | Slide-based visual presentation                    |
| `pandas`                  | Data manipulation (if needed in future extensions) |

---

## 🧪 Installation & Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/portfolio_with_chatbot.git
cd portfolio_with_chatbot
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 🌍 Deployment

This portfolio is deployed using **Render** on the free tier.

- Auto-sleeps after 15 minutes of inactivity
- Cold starts may cause initial delay
- Uptime can be maintained using external pingers like UptimeRobot

---

## 📌 Highlights

- ✅ Clean and professional UI
- 🤖 Smart AI integration to engage recruiters or visitors
- 🧩 Easily customizable sections for future updates
- 💬 Real-time chatbot as an engaging element in a portfolio
