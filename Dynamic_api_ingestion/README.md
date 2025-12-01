# MetaForge

A dynamic, metadata-driven full-stack application that can ingest any public API, parse a custom schema, generate SQLAlchemy models on the fly, and populate a brand‑new SQLite database — all through a simple UI.

This project demonstrates:
- Dynamic schema parsing  
- Automatic database regeneration (RESET DB feature)  
- Fetching & validating external API data  
- Full‑stack React + Flask architecture  
- Clean separation of backend logic for metadata, ingestion, and DB generation  

---

## Features

###  1. **Dynamic Metadata Parsing**
Define your schema in the UI:
```
id: int primary_key  
name: string unique  
height: int  
```

Backend auto‑generates:
- SQLAlchemy model  
- SQLite table  
- Validation rules  

###  2. **RESET Database Button**
One‑click “Reset DB” allows you to:
- Drop old tables  
- Generate a new schema  
- Rebuild entire DB with new structure  

Perfect for testing API → DB ingestion pipelines.

###  3. **API Ingestion**
Provide any API URL (e.g. Pokémon API, Star Wars API):
```
https://pokeapi.co/api/v2/pokemon/
```

Backend fetches the first object to infer shape and validate against your schema.

###  4. **Auto-Populates Database**
Once schema is validated:
- Fetch API data  
- Convert fields  
- Insert rows into SQLite  
- Provide GET endpoints to query data  

---

##  Project Structure

```
MetaForge/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── models.py
│   ├── handleMetadata.py
│   ├── handle_query.py
│   ├── get_files.py
│   ├── mydatabase.db
│   └── requirements.txt
│
└── frontend/
    ├── src/
    │   ├── pages/
    │   │   ├── Home.jsx
    │   │   └── CreateMetadata.jsx
    │   ├── Layout.jsx
    │   ├── App.jsx
    │   └── index.css
    ├── package.json
    └── vite.config.js
```

---

##  Tech Stack

### **Backend (Flask)**  
- Flask  
- SQLAlchemy  
- Flask‑CORS  
- Requests  
- Dynamic model generation  

### **Frontend (React + Vite)**  
- React Router  
- Fetch API  
- clean CSS  
- Minimal UI focused on functionality  

---

## Quick Start

### Clone the repo
```
git clone https://github.com/YOURUSERNAME/MetaForge.git
cd MetaForge
```

### Backend Setup
```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Frontend Setup
```
cd frontend
npm install
npm run dev
```

---

##  Usage

### Step 1 — Add Metadata
Go to **/createMetadata** and input schema:
```
id: int primary_key
name: string unique
height: int
```

### Step 2 — Provide API URL  
Example:
```
https://swapi.dev/api/people/
```

### Step 3 — Reset DB  
Click **RESET** to rebuild database.

### Step 4 — Create  
System generates schema → fetches API → inserts rows.  
You can now hit:
```
GET /data
```
or whatever route you added.

---

##  Contributing
Pull requests are welcome.  
If you find bugs in dynamic model generation, feel free to open an issue.

---

##  License
MIT License © 2025 Rishabh Narula
