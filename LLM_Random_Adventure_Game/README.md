# React + FastAPI LLM Game
A fully interactive AI-powered story adventure game with a complete **FastAPI backend** and **React frontend**.

## 🎮 Project Overview
This project is a full‑stack interactive game powered by LLMs. Players navigate AI‑generated branching stories with multiple decisions, dynamic endings, and an engaging frontend interface.

The game includes:
- Fully built **React UI**
- FastAPI backend with structured LLM story generation
- Dynamic branching nodes
- Win/Lose/Neutral endings
- Smooth, modern gameplay experience

---

## 🧠 Key Features

### 🖥 Frontend (React + TypeScript)
- Built fully in **React + TS**
- Styled with **TailwindCSS**
- Interactive story viewer UI  
- Button‑based navigation between story nodes
- Axios-based API integration
- Loading & error boundaries
- Modular folder structure (components, hooks, API layer)

### ⚙️ Backend (FastAPI)
- LLM‑powered story generator endpoint
- Pydantic data models for:
  - Story
  - StoryNode
  - StoryOption
- Clean, extensible architecture  
- Uvicorn for local development  
- Supports any LLM backend (OpenAI or custom)

### 🎮 Gameplay System
- Branching decisions at each step  
- Multiple endings  
- Persistent game state in frontend  
- Replayable with alternate outcomes  

---

## 🛠 Tech Stack

### **Frontend**
- React (TypeScript)
- TailwindCSS
- Axios
- Vite

### **Backend**
- FastAPI
- Pydantic
- Uvicorn
- Optional: OpenAI GPT models

### **Deployment**
- Frontend → Vercel / Netlify  
- Backend → Render / Railway / EC2  
- Docker‑ready

---

## 📦 Getting Started

### 1️⃣ Clone Repository
```
git clone https://github.com/rishu16111996/Portfolio.git
cd Portfolio/LLMGame
```

---

## 🚀 Backend Setup
### Install dependencies
```
pip install -r requirements.txt
```

### Run FastAPI
```
uvicorn main:app --reload
```

Docs: http://localhost:8000/docs

---

## 🎨 Frontend Setup
### Install dependencies
```
cd frontend
npm install
```

### Run React App
```
npm run dev
```

Open in browser:
```
http://localhost:5173
```

---

## 🧩 Project Structure
```
LLMGame/
├── backend/
│   ├── main.py
│   └── core/
│       ├── model.py
│       ├── generator.py
│       └── utils.py
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── api/
│   │   ├── hooks/
│   │   └── styles/
│   ├── vite.config.ts
│   └── package.json
│
├── data/
├── requirements.txt
└── README.md
```

---

## ✅ What I Built

### **Frontend**
- Designed clean, responsive UI  
- React logic for rendering story nodes  
- Implemented API service using Axios  
- Added interactive gameplay flow  
- Modularized components, hooks, utilities  

### **Backend**
- Complete FastAPI story generation endpoint  
- Structured Pydantic models  
- Integrated branching story logic  
- Flexible generator system for pluggable LLMs  

### **Full‑Stack**
- Created seamless frontend ↔ backend flow  
- Modern UI + robust API  
- Ready for future gameplay expansions  

---

## 🔮 Future Enhancements
- Authentication + user profiles  
- Save game progress  
- Story history visualization  
- Leaderboard or multiplayer mode  
- Mobile version with React Native  
- Voice-based story interactions  

---

## 📄 License
MIT License

---

## 📬 Contact
For questions or collaborations:  
**rishabhnar1996@gmail.com**
