# RAG PDF Ingest Chatbot

This project is a simple Retrieval Augmented Generation application that ingests PDF files and allows you to ask questions about their content. It combines a FastAPI backend, an Inngest workflow for background processing, and a Streamlit frontend for interacting with the system.

The goal is to provide a lightweight, self-contained example of how to build a RAG pipeline end to end. You upload a PDF, the backend extracts and embeds the text, stores it in a vector database, and the chatbot answers your questions using context retrieved from the document.

## Features

### PDF Upload and Ingestion
You can upload a PDF from the Streamlit interface. The backend extracts the text, splits it into chunks, embeds each chunk, and stores them in Qdrant. Inngest is used to run the ingestion workflow asynchronously so that the API remains responsive.

### Question Answering
You can ask any question related to the uploaded document. The FastAPI service retrieves relevant chunks from the vector store, builds a prompt with context, and generates an answer using your selected model.

### Simple and Clean Frontend
The Streamlit app provides a minimal interface where you can upload the PDF, see ingestion progress, and chat with the document.

### Modular Backend
The backend is organized into components for ingestion, storage, embedding, and retrieval so that each part can be replaced or extended. This makes the project a good starting point for building more advanced RAG systems.

## Architecture Overview

The project consists of three main components.

1. FastAPI backend  
   Handles ingestion requests, text extraction, embedding, storage, and question answering.

2. Inngest workflow  
   Runs ingestion as a background job so that long PDF processing does not block the API thread.

3. Streamlit frontend  
   A simple UI for uploading files and chatting with the system.

A vector database such as Qdrant is used to store embeddings and retrieve similar chunks.

## How It Works

1. Upload a PDF from the Streamlit app.  
2. The file is sent to the FastAPI backend.  
3. The backend sends an ingestion event to Inngest and immediately returns.  
4. Inngest runs the ingestion flow which extracts text, chunks it, and creates embeddings.  
5. The chunks and embeddings are stored in the vector database.  
6. When you ask a question, the backend retrieves the top matches from Qdrant and builds a context.  
7. The model generates an answer grounded in the retrieved context.

## Tech Stack

- Python  
- FastAPI  
- Streamlit  
- Inngest  
- Qdrant  
- PyPDF  
- OpenAI embeddings and models

## Setup Instructions

Clone the repository

```
git clone https://github.com/rishu16111996/Portfolio.git
cd Portfolio/RAG_PDF_ingest_Chatbot
```

Create and activate a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the backend

```
uvicorn backend.main:app --reload
```

Start Inngest dev server in a separate terminal

```
inngest dev
```

Run the Streamlit frontend

```
streamlit run app.py
```

Make sure Qdrant is running locally. You can run it using Docker

```
docker run -p 6333:6333 qdrant/qdrant
```

## Project Structure

```
backend/
    main.py
    ingestion/
    storage/
    embeddings/
    workflows/
streamlit_app.py
```

Each module is kept small and focused so you can navigate and extend the code easily.

## Future Improvements

- Add multi document support  
- Add persistent chat history  
- Switch to async ingestion for multi user workloads  
- Add model configuration and caching  
- Deploy the full stack to the cloud

## License

This project is released under the MIT License.
