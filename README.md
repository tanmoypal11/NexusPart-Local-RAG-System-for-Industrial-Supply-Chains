🛠️ NexusPart: Local RAG System for Industrial Supply Chains
🚀 Project Overview

NexusPart is a fully local, GPU-accelerated Retrieval-Augmented Generation (RAG) system designed for industrial procurement and engineering teams.

It performs semantic search over proprietary industrial parts data and generates explainable substitution recommendations using a locally deployed Large Language Model (LLM).

The system ensures data privacy, engineering-grade reasoning, and low-latency AI responses — all without cloud dependency.

🏭 Problem Statement

Engineering and procurement teams often struggle to find safe substitute components during:

Supply chain disruptions

Part obsolescence

Maintenance and repair operations

Emergency procurement scenarios

Traditional keyword search fails to understand technical meaning and specification similarity.

NexusPart solves this using semantic vector search + LLM-based reasoning.

🧠 System Architecture
Phase 1 — Data Intelligence

Load and audit industrial parts dataset

Perform EDA and missing value analysis

Clean and normalize technical descriptions

Standardize measurement units

Create structured combined_text context field

Phase 2 — Vector Search

Generate embeddings using Hugging Face (all-MiniLM-L6-v2)

Store vectors in ChromaDB (local persistent database)

Enable cosine similarity semantic retrieval

Phase 3 — RAG Pipeline

User enters query

Retrieve top-K similar parts

Inject retrieved specs into LLM prompt

Generate justified substitution explanation

Phase 4 — AI Dashboard

Built using Streamlit

Interactive query interface

Displays retrieved reference parts

Engineering-grade natural language analysis

⚙️ Tech Stack

LLM: Llama 3 (via Ollama)

Vector Database: ChromaDB

Embeddings: Hugging Face Sentence Transformers

UI Framework: Streamlit

Language: Python

Acceleration: CUDA (GPU-enabled local inference)

📊 Key Features

Fully local AI deployment (no cloud dependency)

Semantic search over technical specifications

Explainable substitution recommendations

Production-style RAG pipeline

Modular and reusable code structure

GPU-accelerated inference

Streamlit-based interactive dashboard

📈 Evaluation Metrics

Retrieval relevance (Top-K similarity quality)

LLM reasoning and justification quality

Response latency

GPU utilization efficiency

End-to-end system integration

📂 Dataset

Source: Proprietary-style industrial parts data

Format: CSV

Contains technical descriptions and specifications

Requires preprocessing and normalization before embedding

Preprocessing includes:

Text normalization

Missing value handling

Noise removal

Context string generation for embedding

🖥️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/your-username/NexusPart.git
cd NexusPart
2️⃣ Install Dependencies
pip install -r requirements.txt

Main dependencies:

streamlit

chromadb

sentence-transformers

ollama

pandas

seaborn

numpy

3️⃣ Start Ollama

Install Ollama and pull Llama 3:

ollama pull llama3:8b

Verify GPU acceleration is enabled.

4️⃣ Run Streamlit App
streamlit run app.py
🗂️ Project Structure
NexusPart/
│
├── app.py                  # Home page
├── pages/
│   └── 1_Search.py         # RAG Search Engine
├── data/
│   └── Parts.csv
├── notebooks/
│   └── EDA.ipynb
├── nexus_part_db/          # ChromaDB persistent storage
└── README.md
🧪 Example Query
Need substitute for 1.6A ceramic fuse used in primary protection.

System retrieves similar parts and generates:

Technical comparison

Spec-based justification

Safety warnings (if applicable)

🎯 Business Impact

Reduces procurement decision time

Mitigates supply chain risk

Enhances engineering productivity

Enables safe and explainable AI recommendations

Protects proprietary data through local deployment

📅 Development Timeline
Week	Task	Deliverable
Week 1	Data cleaning & EDA	Cleaned dataset
Week 1	Embeddings & Vector DB	Local index
Week 2	RAG pipeline	Substitution reasoning
Week 2	Streamlit deployment	Interactive AI tool
🧩 Future Improvements

Confidence scoring system

Spec comparison table

Structured JSON output

Logging & monitoring

Multi-model benchmarking

Docker containerization

🏁 Final Outcome

NexusPart demonstrates:

Practical RAG implementation

Local LLM deployment

Industrial AI application

MLOps workflow understanding

End-to-end system integration

This project bridges Generative AI, Supply Chain Intelligence, and Industrial Engineering Decision Support.
