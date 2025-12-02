import os
import sys
from dotenv import load_dotenv
from pypdf import PdfReader
from openai import OpenAI
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    SentenceTransformersTokenTextSplitter,
)
import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

from helper_utils import word_wrap



load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


DATA_DIR = "data"
DB_DIR = "storage/chroma"
COLLECTION_NAME = "rna_splicing"
EMBED_CHUNK_SIZE = 256


def load_pdfs(data_dir=DATA_DIR):
    pdf_texts = []

    for filename in os.listdir(data_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(data_dir, filename)
            reader = PdfReader(pdf_path)

            for page in reader.pages:
                text = page.extract_text()
                if text:
                    pdf_texts.append((filename, text.strip()))
    return pdf_texts



def split_into_chunks(pdf_texts):
    character_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap=0,
    )

    merged_text = "\n\n".join([t[1] for t in pdf_texts])
    character_chunks = character_splitter.split_text(merged_text)

    token_splitter = SentenceTransformersTokenTextSplitter(
        chunk_overlap=0, tokens_per_chunk=EMBED_CHUNK_SIZE
    )

    final_chunks = []
    for chunk in character_chunks:
        final_chunks.extend(token_splitter.split_text(chunk))

    return final_chunks



def load_or_create_chroma(chunks, persist_dir=DB_DIR):
    embedding_function = SentenceTransformerEmbeddingFunction()

    chroma_client = chromadb.PersistentClient(path=persist_dir)

    try:
        collection = chroma_client.get_collection(
            COLLECTION_NAME, embedding_function=embedding_function
        )
        print("Loaded existing Chroma collection.")
        return collection

    except:
        print("Creating new Chroma collection...")
        collection = chroma_client.create_collection(
            name=COLLECTION_NAME,
            embedding_function=embedding_function,
        )
        ids = [str(i) for i in range(len(chunks))]
        collection.add(ids=ids, documents=chunks)
        print(f"✨ Added {len(chunks)} chunks.")
        return collection



def augment_query(query, model="gpt-4.1-mini"):
    prompt = """You are an expert computational biologist specializing in RNA splicing.
Provide a hypothetical answer that might appear in an RNA splicing paper.
This will be used to enhance semantic search."""
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": query},
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content



def search_docs(collection, query, n_results=5):
    results = collection.query(
        query_texts=[query],
        n_results=n_results,
        include=["documents", "metadatas"],
    )
    docs = results["documents"][0]
    return docs



def answer_with_context(query, retrieved_docs, model="gpt-4.1"):
    context = "\n\n---\n".join(retrieved_docs)

    messages = [
        {
            "role": "system",
            "content": "You are an RNA splicing domain expert. Answer strictly based on context.",
        },
        {
            "role": "user",
            "content": f"Question: {query}\n\nContext:\n{context}\n\nAnswer:",
        },
    ]

    resp = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return resp.choices[0].message.content



def main():
    if len(sys.argv) < 2:
        print("Usage:")
        return

    user_query = sys.argv[1]
    print(f"Query: {user_query}")

    pdf_texts = load_pdfs()
    chunks = split_into_chunks(pdf_texts)
    collection = load_or_create_chroma(chunks)

    hypo = augment_query(user_query)
    joint_query = f"{user_query} {hypo}"

    retrieved = search_docs(collection, joint_query)
    final_answer = answer_with_context(user_query, retrieved)

    print("\n========== FINAL ANSWER ==========\n")
    print(word_wrap(final_answer, 100))

    print("\n========== SOURCES USED ==========\n")
    for doc in retrieved:
        print(word_wrap(doc[:300], 100)) 


if __name__ == "__main__":
    main()
