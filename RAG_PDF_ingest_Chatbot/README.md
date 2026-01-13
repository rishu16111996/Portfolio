# RAG PDF Ingest Chatbot

This project is a simple Retrieval-Augmented Generation (RAG) application that lets you upload PDFs, ingest them into a vector database, and ask questions about their content. The backend is built with FastAPI and Inngest, and the frontend uses Streamlit. The whole environment is managed with `uv` instead of pip.

## How It Works

1. You upload one or more PDF files through the Streamlit interface.
2. The backend extracts text, chunks it, embeds it, and stores it in a vector database.
3. When you ask a question, the backend retrieves the most relevant chunks and generates an answer based on that context.
4. Inngest handles background tasks such as PDF ingestion and embedding so the app stays fast and responsive.

## Project Structure

```
RAG_PDF_ingest_Chatbot/
    backend/
        app/
        embeddings/
        routes/
        utils/
        inngest/
        streamlit_app.py
```

## Features

- Upload PDFs and process them asynchronously
- Background ingestion pipeline using Inngest
- Vector-based semantic search
- FastAPI backend API
- Streamlit frontend for interacting with the chatbot
- Environment managed using uv for faster dependency handling

## Running the Project

### 1. Install dependencies with uv

```
uv sync
```

This creates and manages the virtual environment automatically.

### 2. Start the backend

```
uv run backend/main.py
```

This launches the FastAPI server.

### 3. Start the Streamlit frontend

```
uv run streamlit run backend/streamlit_app.py
```

### 4. Use the App

1. Open the Streamlit page in your browser
2. Upload your PDF
3. Ask any question about the document

## Notes

- Make sure your FastAPI backend is running before launching the Streamlit UI.
- You can modify the embedding model or chunking strategy inside the backend code.
- Inngest must be running for background tasks to work properly.

