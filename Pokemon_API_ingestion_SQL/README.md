# Full Stack Flask + React + SQL App

Description: I built this lightweight Full-Stack SQL Playground to quickly run and test SQL commands locally — without the need for installing heavy database managers (~500 MB). This app runs entirely on your machine with under 20 MB of setup, supports your own uploaded datasets, and provides an instant environment to experiment with queries, visualize tables, and build data logic fast.

While developing this project, I realized there wasn’t a simple website or tool that lets users upload their own data and run live SQL queries in a minimal, offline-first setup — so I designed this one to fill that gap. The focus here is functionality over styling: it’s a raw, efficient, and fully extensible foundation for rapid query testing, but it can easily be styled or scaled into a polished production app as needed.


This project is a full-stack web application with:
- Flask as the backend (Python)  
- React as the frontend (JavaScript)  
- SQLite as the database  

The repository is organized into two main folders:  
- `backend/` — Flask server & database  
- `frontend/` — React app

---

## Backend Setup (Flask + SQLite)

### 1. Create and activate a virtual environment
```bash
cd backend
python -m venv venv
```

#### macOS / Linux
```bash
source venv/bin/activate
```

#### Windows (PowerShell)
```bash
venv\Scripts\Activate.ps1
```

#### Go back to main directory or copy requirment.txt here
```bash
cd ..
```

#### Instal dependencies
```bash
pip install -r requirements.txt
```


#### From backend folder run
```bash
python main.py
```

#### Default URL
```bash
http://127.0.0.1:5000
```

## Frontend Setup (React + Vite)
```bash
cd frontend
```

#### Install server
```bash
npm install
```

#### start server
```bash
npm run dev
```

#### Defualt URL
```bash
http://localhost:5173
```

# How to run the application

1. Copy paste the URL: http://localhost:5173
2. Make sure backend is also running
3. It automatically generates the SQL data in background on first run, if it doesn't press Generate Data, with link already given or use https://pokeapi.co/api/v2/pokemon/ (If you generate again, it will take 10 to 20 sec just wait and it will show alert that data is complete)
4. It will show original table.
5. You can add any SQL query in box and press send query, to run the query on data
6. Or you can press Generate button to show the question asked in challenge.





