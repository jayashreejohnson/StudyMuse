
import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import tempfile
import time
# --- Custom Pastel Styling ---
st.markdown("""
    <style>
    /* Background in pastel pink */
    .stApp {
        background-color: #fff8f4;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        background-color: #ffeaf2;
        border-radius: 10px;
        padding: 4px;
    }

    /* Selected tab */
    .stTabs [aria-selected="true"] {
        background-color: #fcd6e2;
        color: black;
        border-radius: 10px;
        font-weight: bold;
    }

    /* Input box */
    input, .stTextInput>div>div>input {
        background-color: #fffafc;
        border: 1px solid #f7b4c2;
        border-radius: 8px;
        padding: 10px;
    }

    /* Subheaders & Titles */
    h1, h2, h3, h4 {
        color: #3f3f3f;
    }

    /* Success message (like Learning Module found) */
    .stAlert-success {
        background-color: #e6fffa;
        color: #264d4a;
    }

    /* Markdown and body text */
    .css-1cpxqw2, .stMarkdown {
        color: #2f2f2f;
    }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="StudyMuse", layout="centered")
st.title("📚 StudyMuse – Visual Memory Aid for Science Students")

tab1, tab2 = st.tabs(["📤 Upload Notes", "🔍 Search Topic"])

# ---------------- Upload Tab ----------------
with tab1:
    st.subheader("Upload notes (PDF or image)")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file:
        file_type = uploaded_file.type

        if "pdf" in file_type:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                doc = fitz.open(tmp_file.name)
                text = ""
                for page in doc:
                    text += page.get_text()
                st.success("✅ Extracted text from PDF:")
                st.write(text[:2000])

        elif "image" in file_type:
            img = Image.open(uploaded_file)
            text = pytesseract.image_to_string(img)
            st.success("✅ Extracted text from image:")
            st.write(text[:2000])

        st.info("✨ Coming soon: Smart AI summaries + topic detection")
# ---------------- Search Tab ----------------
with tab2:
    st.subheader("Search Biotech/Science Topic")
    topic = st.text_input("Enter a topic (e.g., PCR, miRNA, CRISPR)")

   if topic:
       with st.spinner("🔎 Searching the depths of science..."):
           time.sleep(1.5)  # Simulate animation pause

        if topic.lower() == "pcr":
           st.success("🧬 Learning Module: Polymerase Chain Reaction (PCR)")

            # --- Section: Deep Summary ---
            st.markdown("### 📋 Detailed Summary of PCR")
            st.markdown("""
            **Polymerase Chain Reaction (PCR)** is a groundbreaking molecular biology technique developed by **Kary Mullis** in 1983. It revolutionized the way we amplify and analyze DNA.

            #### 🔬 What is PCR?
            A method to generate millions to billions of copies of a specific DNA segment using a thermal cycler.

            #### 🧠 Fun Facts:
            - Invented during a drive on the California coast
            - Won the **Nobel Prize in Chemistry** in 1993
            - Used in everything from ancestry kits to COVID-19 testing

            #### ⚙️ Components:
            - Template DNA
            - Primers (short DNA sequences that flank the target)
            - Taq DNA Polymerase (heat-resistant enzyme)
            - dNTPs (building blocks: A, T, G, C)
            - Buffer with MgCl₂

            #### 🔁 Steps in a Cycle:
            1. **Denaturation (94–96°C)** – DNA strands separate
            2. **Annealing (50–65°C)** – Primers attach
            3. **Extension (72°C)** – Taq polymerase builds new DNA

            #### ✅ Advantages:
            - Rapid and cost-effective
            - Requires minimal sample
            - High specificity and sensitivity
            - Versatile across fields (medical, forensics, agriculture)

            #### 🚫 Limitations:
            - Contamination risk
            - Requires primer sequence knowledge
            - Not ideal for long DNA fragments

            #### 🔬 Applications:
            - 🧬 Genetic diagnostics (e.g., BRCA mutation testing)
            - 🦠 Pathogen detection (e.g., COVID-19)
            - 🔍 Forensic DNA profiling
            - 🌾 Detection of GMOs in food
            - 🧪 Research cloning & gene expression
            """)

            # --- Diagrams ---
            st.markdown("### 🖼️ Visual Diagrams")
            col1, col2 = st.columns(2)
            with col1:
                st.image(
                    "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR1.jpeg",
                    caption="PCR Workflow Overview", use_container_width=True)
            with col2:
                st.image(
                    "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR2.jpg",
                    caption="PCR Steps Simplified", use_container_width=True)

            col3, col4 = st.columns(2)
            with col3:
                st.image(
                    "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR4.png",
                    caption="DNA Polymerase Mechanism", use_container_width=True)
            with col4:
                st.image(
                    "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR3.jpg",
                    caption="Visual Breakdown of Viral RNA Extraction & Detection", use_container_width=True)

            st.image(
                "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR5.jpeg",
                caption="Thermal Profile of PCR", use_container_width=True)

            # --- Videos ---
            st.markdown("### 🎥 Watch & Learn")
            st.video("https://www.youtube.com/embed/2KoLnIwoZKU")
            st.video("https://www.youtube.com/embed/mOKb0Pd_Rac")

            # --- Interactive Quiz ---
            st.markdown("### 🧠 Quiz Time")
            if "submitted" not in st.session_state:
                st.session_state["submitted"] = False

            with st.form("quiz_form"):
                q1 = st.radio("1. What does PCR stand for?",
                              ["Protein Chain Reaction", "Polymerase Chain Reaction", "Primer Cloning Reaction"], index=None)
                q2 = st.radio("2. What enzyme is used in PCR?",
                              ["DNA Ligase", "RNA Polymerase", "Taq Polymerase"], index=None)
                q3 = st.radio("3. What temperature is used in annealing?",
                              ["30–40°C", "50–65°C", "75–85°C"], index=None)
                q4 = st.radio("4. What happens during extension?",
                              ["DNA separates", "Primers bind", "Taq builds new DNA"], index=None)
                submit = st.form_submit_button("Submit Answers")

            if submit:
                st.markdown("### ✅ Your Results")
                st.markdown(f"**Q1:** {'✅ Correct' if q1 == 'Polymerase Chain Reaction' else '❌ Incorrect'}")
                st.markdown(f"**Q2:** {'✅ Correct' if q2 == 'Taq Polymerase' else '❌ Incorrect'}")
                st.markdown(f"**Q3:** {'✅ Correct' if q3 == '50–65°C' else '❌ Incorrect'}")
                st.markdown(f"**Q4:** {'✅ Correct' if q4 == 'Taq builds new DNA' else '❌ Incorrect'}")

            st.info("🧪 Stay tuned for advanced scoring, saved progress, and more topics!")
        else:
            st.warning(f"No visual module yet for: {topic}")

