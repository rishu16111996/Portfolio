# FastAPI + Streamlit Photo/Video Sharing App

## 🚀 Overview
This project is a web application built using **FastAPI** (backend API) and **Streamlit** (frontend UI) that allows users to upload, view, and share photos/videos.  

## 🔥 Features
- Upload images and videos through API  
- View all uploaded media in Streamlit  
- Clean, simple UI for testing the backend quickly  
- Supports multiple file types  
- Easy-to-extend structure for additional features  

## 🛠️ Tech Stack
- **FastAPI** – backend REST API  
- **Streamlit** – frontend interface  
- **Python 3.10+**  
- **Uvicorn** – ASGI server  
- Local filesystem for storage (customizable)  

## 📦 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Backend (FastAPI)
```bash
uvicorn main:app --reload
```

### 4️⃣ Run Frontend (Streamlit)
```bash
streamlit run frontend.py
```

Visit:  
**http://localhost:8501** → Streamlit  
**http://localhost:8000/docs** → FastAPI Swagger docs  

## 📁 Project Structure
```
├── app
│   ├── main.py
│   ├── api
│   ├── models
│   ├── services
│   └── storage
├── frontend.py
├── requirements.txt
└── README.md
```

## ✅ What I Built / Customized
- Recreated the API using FastAPI  
- Built a Streamlit UI to test uploads  
- Structured code into clean modules  
- Added my own language + UI tweaks  
- Improved file handling logic  
- Made the repo simple for anyone to clone and run instantly  

## 🔧 Future Plans
- User authentication  
- Cloud storage (AWS S3 / GCP)  
- Better video preview support  
- Thumbnail generation  
- Streamlit dark mode  

## 📄 License
MIT License  

## 📬 Contact
Feel free to reach out or open an issue!
