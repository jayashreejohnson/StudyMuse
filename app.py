
import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import tempfile

st.set_page_config(page_title="StudyMuse", layout="centered")
st.title("📚 StudyMuse – Visual Memory Aid for Science Students")
st.markdown("""
    <style>
    /* Entire app background & text */
    .main {
        background-color: #fdf6f0;
        color: #333;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Title and section headings */
    h1, h2, h3 {
        color: #665c84;
    }

    /* Tabs */
    .stTabs [data-baseweb="tab"] {
        background-color: #fde4ec;
        border-radius: 5px;
        color: #493256;
    }
    .stTabs [aria-selected="true"] {
        background-color: #fbcadf;
        font-weight: bold;
    }

    /* File uploader and input boxes */
    .stFileUploader, .stTextInput, .stTextArea {
        background-color: #fff0f6;
        border-radius: 8px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #f8bbd0;
        color: white;
        border: none;
        border-radius: 6px;
    }

    /* Info and success alerts */
    .stAlert {
        background-color: #ffe6f0;
        border-left: 5px solid #f48fb1;
    }

    /* Markdown containers */
    .markdown-text-container {
        background-color: #fff7fb;
        padding: 1rem;
        border-radius: 12px;
        border: 1px solid #f7c3d4;
    }

    /* Quiz radio options */
    .stRadio > div {
        background-color: #fff5f9;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

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

