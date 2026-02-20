import streamlit as st
import chromadb
import ollama

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="NexusPart Smart Search", layout="wide")
st.title("🛠️ NexusPart: Industrial Command Center")

# Your E: drive path
DB_PATH = r"E:\Desktop\GUVI\Project\NexusPart Local RAG System for Industrial Supply Chains\nexus_part_db"

# --- 2. DATA LOADERS ---
@st.cache_resource
def get_collection():
    client = chromadb.PersistentClient(path=DB_PATH)
    return client.get_collection(name="industrial_components")

collection = get_collection()

# Get all IDs for the dropdown list
def get_all_ids():
    data = collection.get()
    return sorted(data['ids'])

part_ids = get_all_ids()

# --- 3. THE RAG ENGINE ---
def run_nexus_engine(user_input):
    # Retrieve top 3 matches from ChromaDB
    results = collection.query(query_texts=[user_input], n_results=3)
    context = "\n\n".join(results['documents'][0])
    
    # Generate Engineering Response via Ollama
    response = ollama.chat(
        model='llama3:8b',
        messages=[
            {'role': 'system', 'content': f"You are an Industrial Engineer. Analyze this data: {context}"},
            {'role': 'user', 'content': user_input}
        ],
        options={'num_ctx': 2048, 'temperature': 0.1}
    )
    return response['message']['content'], results['documents'][0]

# --- 4. THE "SINGLE BOX" UI ---
# We use a selectbox that allows typing NEW text (accept_new_options=True)
st.markdown("### 🔍 Search or Select Part")
query = st.selectbox(
    "Type a Part ID or ask a technical question:",
    options=part_ids,
    index=None,
    placeholder="Example: 'A102' or 'Find ceramic substitutes for 1.6A fuses'...",
    accept_new_options=True  # THIS MERGES SEARCH AND DROPDOWN
)

col1, col2 = st.columns([2, 1])

with col1:
    if query:
        st.info(f"Processing: **{query}**")
        with st.spinner("Analyzing Database..."):
            answer, docs = run_nexus_engine(query)
            st.markdown("---")
            st.subheader("AI Analysis")
            st.write(answer)
            st.session_state.last_docs = docs
    else:
        st.write("Waiting for input... Use the box above to start.")

with col2:
    st.subheader("📋 Source Data")
    if "last_docs" in st.session_state:
        for i, doc in enumerate(st.session_state.last_docs):
            with st.expander(f"Reference Part {i+1}"):
                st.write(doc)
    else:
        st.info("Technical specs will appear here once you search.")