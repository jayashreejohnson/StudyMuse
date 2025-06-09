import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import tempfile

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
        if topic.lower() == "pcr":
            st.success("🧬 Learning Module: Polymerase Chain Reaction (PCR)")

            # --- Section: Deep Summary ---
            st.markdown("### 📋 Detailed Summary of PCR")
            st.markdown("""
            **Polymerase Chain Reaction (PCR)** is a revolutionary molecular biology technique used to selectively amplify DNA. It enables researchers to create millions of copies of a specific DNA segment from a minimal starting amount.

            #### 🔬 Why is PCR Important?
            - Makes DNA analysis faster, cheaper, and more accessible
            - Enables genetic testing without needing large tissue samples
            - Powers genomics, diagnostics, forensics, and more

            #### 🧪 Core Principle
            Mimics natural DNA replication using a **thermal cycler** and **heat-stable DNA polymerase** (Taq). Each cycle doubles the DNA — ~1 billion copies in 30 cycles.

            #### ⚙️ Components
            - Template DNA
            - Primers
            - Taq Polymerase (from *Thermus aquaticus*)
            - dNTPs (A, T, G, C)
            - Buffer & MgCl₂

            #### 🔁 Workflow
            1. **Denaturation (94–96°C)** – DNA strands separate
            2. **Annealing (50–65°C)** – Primers bind to target
            3. **Extension (72°C)** – New DNA built by Taq

            #### 🧬 Who Invented It?
            - Kary Mullis, 1983 — Nobel Prize in Chemistry, 1993

            #### 🚫 Limitations
            - Sensitive to contamination
            - Requires primer knowledge
            - Not ideal for long DNA sequences
            """)

            # --- Applications ---
            st.markdown("### 💡 Applications of PCR")
            st.markdown("""
            - 🧪 Disease diagnostics (e.g., COVID-19, HIV)
            - 🔬 DNA fingerprinting in forensics
            - 🧬 Detecting mutations in genetic diseases
            - 🌽 GMO detection in agriculture
            - 🧫 Gene cloning & expression research
            """)

            # --- Diagrams ---
            st.markdown("### 🖼️ Visual Diagrams")
            cols = st.columns(2)
            images = [
                ("PCR Workflow Overview", "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR1.jpeg"),
                ("PCR Steps Simplified", "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR2.jpg"),
                ("Visual Breakdown of Viral RNA Extraction & Detection", "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR3.jpg"),
                ("DNA Polymerase Mechanism", "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR4.png"),
                ("Thermal Profile of PCR", "https://raw.githubusercontent.com/jayashreejohnson/StudyMuse/main/assets/pcr/PCR5.jpeg")
            ]
            for i, (caption, url) in enumerate(images):
                cols[i % 2].image(url, caption=caption, use_container_width=True)

            # --- Videos ---
            st.markdown("### 🎥 Watch & Learn")
            st.video("https://www.youtube.com/embed/2KoLnIwoZKU")
            st.video("https://www.youtube.com/embed/iQsu3Kz9NYo")
            st.video("https://www.youtube.com/embed/FZ6Lgtp6wTA")

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

