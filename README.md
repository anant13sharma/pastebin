# 📋 Pastebin by Anant

A clean, mobile-responsive Pastebin clone built with Django and Bootstrap 5 — styled with a soothing animated gradient color scheme. Create and share text/code snippets effortlessly.

---

## 🔗 Live Demo
**Hosted on Render**  
🌐 [https://pastebin-django.onrender.com](https://pastebin-django.onrender.com)

---

## 📸 Features

- 🔒 Secure paste submission with CSRF protection
- 🌈 Custom animated background using soft pastel color palette
- 📱 Fully responsive on all devices (iPhones, tablets, desktops)
- 💾 Stores title, author, description, and body text
- 📤 Copy-to-clipboard functionality
- 🛠 Auto-migration setup for Render Free Tier

---

## 🎨 Tech Stack

- **Frontend:** HTML5, Bootstrap 5, CSS3
- **Backend:** Django 4
- **Database:** PostgreSQL (Render-hosted)
- **Deployment:** Render (Free Web Service + Database)
- **Clipboard API:** Native browser clipboard for copying pastes

---

## ⚙️ Setup Locally

```bash
# 1. Clone the repository
git clone https://github.com/anant13sharma/pastebin.git
cd pastebin

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file
touch .env
