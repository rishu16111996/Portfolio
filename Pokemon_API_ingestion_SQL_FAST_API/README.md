# 📦 PokeAPI SQLite Dashboard  
_A full-stack FastAPI + React + Tailwind project demonstrating data ingestion, SQL analytics, API design, and modern frontend engineering._

![banner](https://dummyimage.com/1200x250/1e293b/10b981&text=PokeAPI+SQLite+Dashboard)

---

## 🚀 Overview

This project ingests **Generation 1 Pokémon (1–151)** from the public **PokeAPI**, normalizes the data into a **SQLite** database, and exposes analytics through a **FastAPI backend** and a **React + Tailwind** dashboard.

It was originally built as a technical challenge requiring:

- SQL schema design  
- data ingestion  
- analytic queries  
- stat ranking via window functions  
- identifying “tanky” Pokémon  
- reporting type combinations  

I expanded it into a production-style full-stack application suitable for portfolios and interviews.

---

## 🧩 Features

### ✅ **Backend (FastAPI)**
- Ingests Pokémon data with stats + types  
- Normalized SQL schema using SQLAlchemy ORM  
- SQLite database with join tables  
- API endpoints for:
  - All Pokémon and stats  
  - Type combinations and counts  
  - Tanky-label assignment  
  - Most tanky Pokémon per type  
  - Rankings via SQL window functions  
- Auto-generated API docs at `/docs`

### 🎨 **Frontend (React + Vite + Tailwind)**
- Modern responsive UI  
- Pokémon table with stats  
- Type combination summary  
- Tankiness analysis using Recharts bar chart  
- Ranking table by type  
- Clean layout and navigation  

---

## 📁 Project Structure

```
pokeapi-sql/
│
├── backend/
│   ├── app/
│   ├── scripts/
│   ├── requirements.txt
│
└── frontend/
    ├── src/
    ├── package.json
    └── vite.config.ts
```

---

## 🗄️ Database Schema

```
pokemon
---------
id (PK)
name
hp
attack
defense
special_attack
special_defense
speed

type
---------
id (PK)
name (unique)

pokemon_type
---------
pokemon_id (FK → pokemon)
type_id (FK → type)
slot (1 or 2)
```

---

## 📊 SQL Logic Highlights

### 🔹 Distinct type combinations  
Uses `GROUP_CONCAT` ordered by slot.

### 🔹 “Tanky” determination  
SQLite-safe MAX over multiple columns:

```sql
SELECT MAX(x) FROM (
    SELECT hp UNION ALL
    SELECT attack UNION ALL
    SELECT defense UNION ALL
    SELECT special_attack UNION ALL
    SELECT special_defense UNION ALL
    SELECT speed
)
```

### 🔹 Rankings via window functions  

```sql
RANK() OVER (
  PARTITION BY t.name
  ORDER BY total_stats DESC
)
```

---

## ⚡ Running the Project

### 1️⃣ Backend Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create and populate the DB:

```bash
python scripts/create_db.py
python scripts/ingest_data.py
```

Run server:

```bash
uvicorn app.main:app --reload --port 8000
```

Docs:

👉 http://localhost:8000/docs

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

App available at:

👉 http://localhost:5173

---

## 🖼️ Screenshots (Add yours)

```
[ ] Pokémon Table  
[ ] Tanky Chart  
[ ] Rankings Page  
[ ] Type Summary  
```

---

## 📈 API Endpoints Summary

| Endpoint | Description |
|---------|-------------|
| `/pokemon` | List all Pokémon + stats + types |
| `/pokemon?type=water` | Filter by type |
| `/pokemon?tanky=true` | Only tanky Pokémon |
| `/stats/type-combos` | Distinct type combinations |
| `/stats/tanky-labels` | Tanky classification |
| `/stats/tanky-types` | Types with most tanky Pokémon |
| `/stats/rankings` | Ranked Pokémon per type |

---

## 🧠 What This Project Demonstrates

✔ Data ingestion workflows  
✔ Database design  
✔ ORM modeling  
✔ SQL joins & window functions  
✔ FastAPI routing & Pydantic  
✔ React component architecture  
✔ Tailwind UI design  
✔ Recharts visualization  
✔ Full-stack engineering  

---

## ⭐ Future Enhancements

- Pokémon detail page with sprites  
- Sorting & filtering  
- Deployment on Vercel / Render  
- Switch SQLite → Postgres for production  

---

## 📬 Contact

**Rishabh Narula**  
