import streamlit as st

st.set_page_config(
    page_title="NexusPart AI",
    page_icon="🛠️",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("🛠️ NexusPart: AI for Industrial Supply Chains")
st.markdown(
"""
### Local RAG-Powered Engineering Intelligence System
A fully local AI system that performs **semantic search** over industrial parts  
and generates **engineering-grade substitution recommendations**.
"""
)

st.divider()

# ---------------- OVERVIEW ----------------
col1, col2 = st.columns([2,1])

with col1:
    st.subheader("📌 Project Overview")
    st.write("""
NexusPart is a **GPU-accelerated Retrieval-Augmented Generation (RAG) system**
designed for industrial procurement and engineering teams.

It allows organizations to search proprietary parts databases and receive
AI-generated justifications for part substitutions while keeping all data local.
    """)

with col2:
    st.subheader("🧠 Core Capabilities")
    st.markdown("""
- Semantic part search  
- Substitute recommendation  
- Local LLM reasoning  
- Explainable AI output  
- Proprietary data safe  
""")

st.divider()

# ---------------- PROBLEM ----------------
st.subheader("🏭 Problem Statement")
st.write("""
Engineering teams often struggle to find substitute components during:
- supply chain disruptions  
- maintenance operations  
- part obsolescence  

Traditional keyword search fails to understand **technical meaning**.
NexusPart solves this using semantic AI reasoning.
""")

# ---------------- USE CASES ----------------
st.subheader("💼 Business Use Cases")

c1, c2, c3, c4, c5 = st.columns(5)

with c1:
    st.markdown("**Procurement decisions**")
    st.caption("AI-assisted sourcing")

with c2:
    st.markdown("**Part substitution**")
    st.caption("Find compatible components")

with c3:
    st.markdown("**Maintenance repair**")
    st.caption("Smart replacement logic")

with c4:
    st.markdown("**Supply chain risk**")
    st.caption("Mitigate shortages")

with c5:
    st.markdown("**Engineering support**")
    st.caption("Spec-based reasoning")


st.divider()

# ---------------- HOW IT WORKS ----------------
st.subheader("⚙️ How It Works")

st.markdown("""
**Step 1 — Vector Search**  
Industrial parts are embedded into a vector database (ChromaDB).

**Step 2 — Retrieval**  
Top-K similar parts are retrieved based on semantic meaning.

**Step 3 — Local LLM Reasoning**  
Llama-3 (via Ollama) analyzes specs and justifies substitutions.

**Step 4 — Streamlit Dashboard**  
Interactive UI for engineers and procurement teams.
""")

st.divider()

# ---------------- TECH STACK ----------------
st.subheader("🧰 Tech Stack")

c1, c2, c3, c4 = st.columns(4)

c1.info("LLM\n\nLlama-3 (Ollama)")
c2.info("Vector DB\n\nChromaDB")
c3.info("Embeddings\n\nHuggingFace")
c4.info("UI\n\nStreamlit")

st.divider()

# ---------------- METRICS ----------------
st.subheader("📊 System Metrics")

m1, m2, m3, m4 = st.columns(4)
m1.metric("Architecture", "Local RAG")
m2.metric("Latency", "Low")
m3.metric("Data Privacy", "100% Local")
m4.metric("Explainability", "High")

st.divider()

# ---------------- NAVIGATION ----------------
st.subheader("🚀 Launch System")

st.success("Use the sidebar to open the **Search Engine**")

st.markdown("""
👉 Go to **Search** page from the sidebar to query parts  
""")

# ---------------- FOOTER ----------------
st.divider()
st.caption("Built for AI-driven industrial decision support")
