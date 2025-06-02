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

    if topic.lower() == "pcr":
        st.success("🧬 Polymerase Chain Reaction (PCR)")

        # --- Definition ---
        st.markdown("### 📌 What is PCR?")
        st.markdown("**PCR (Polymerase Chain Reaction)** is a technique used to amplify specific DNA sequences in vitro, generating millions of copies from a small DNA sample.")

        # --- History ---
        st.markdown("### 🧬 Who developed it?")
        st.markdown("- Invented by **Kary Mullis** in 1983\n- Revolutionized molecular biology\n- Awarded the **Nobel Prize in Chemistry (1993)**")

        # --- Applications ---
        st.markdown("### 💡 Applications of PCR")
        st.markdown("""
        - 🧪 Diagnosing infectious diseases (e.g., COVID-19, HIV)
        - 🧬 Cloning and gene expression analysis
        - 🔬 Forensic DNA fingerprinting
        - 🌱 Genetically modified organisms (GMO) detection
        - 🧫 Cancer mutation detection
        """)

        # --- Key Components ---
        st.markdown("### 🔧 PCR Components")
        st.markdown("""
        - **Template DNA**: The DNA to be copied
        - **Primers**: Short sequences that initiate replication
        - **Taq Polymerase**: Heat-stable enzyme that builds DNA
        - **dNTPs**: Nucleotide building blocks (A, T, G, C)
        - **Buffer & Mg²⁺**: Maintain pH and enzyme activity
        """)

        # --- 3-Step Mechanism ---
        st.markdown("### 🔄 PCR Mechanism (Cycle)")
        st.markdown("""
        1. **Denaturation** (94–96°C): DNA strands separate
        2. **Annealing** (50–65°C): Primers bind to target
        3. **Extension** (72°C): Taq polymerase builds new strands
        """)

        # --- Videos ---
        st.markdown("### 🎥 Learn PCR Visually (Basic → Advanced)")

        st.markdown("**📘 Intro to PCR**")
        st.video("https://www.youtube.com/watch?v=2KoLnIwoZKU")

        st.markdown("**📗 PCR Explained with Animation**")
        st.video("https://www.youtube.com/watch?v=_YgXcJ4n-kQ")

        st.markdown("**📕 Advanced PCR Variants**")
        st.video("https://www.youtube.com/watch?v=3t-Nm4qAC8M")

        # --- Diagrams ---
        st.markdown("### 🖼️ Diagrams & Flowcharts")

        st.image("https://i.imgur.com/nZB9QyM.png", caption="PCR Flow Overview")
        st.image("https://i.imgur.com/w3VFIcy.png", caption="PCR 3-Step Cycle")
        st.image("https://i.imgur.com/9v6FzAW.png", caption="PCR Setup in Tube")
        st.image("https://i.imgur.com/UmcMbv1.png", caption="Amplification Rounds")
        st.image("https://i.imgur.com/6pSFXbP.png", caption="Taq Polymerase Mechanism")

        st.markdown("💡 **Tip:** Click the sidebar to try other topics like CRISPR or miRNA soon!")

# --- QUIZ SECTION ---
st.markdown("### 🧠 Quiz Time: Test Your PCR Knowledge")

st.markdown("#### 🧪 Basic Level")

q1 = st.radio("1. What does PCR stand for?", 
              ["Protein Chain Reaction", "Polymerase Chain Reaction", "Primer Cloning Reaction"], key="q1")
if q1 == "Polymerase Chain Reaction":
    st.success("✅ Correct!")
elif q1:
    st.error("❌ Oops! It stands for Polymerase Chain Reaction.")

q2 = st.radio("2. What enzyme is used in PCR?", 
              ["DNA Ligase", "RNA Polymerase", "Taq Polymerase"], key="q2")
if q2 == "Taq Polymerase":
    st.success("✅ Correct!")
elif q2:
    st.error("❌ Nope. It's Taq Polymerase — a heat-stable DNA polymerase.")

# --- ADVANCED QUIZ ---
st.markdown("#### 🔬 Advanced Level")

q3 = st.radio("3. At what temperature does annealing usually occur?", 
              ["30–40°C", "50–65°C", "75–85°C"], key="q3")
if q3 == "50–65°C":
    st.success("✅ Correct!")
elif q3:
    st.error("❌ Not quite. Annealing happens around 50–65°C.")

q4 = st.radio("4. What happens during the extension phase?", 
              ["DNA strands separate", 
               "Primers bind to template", 
               "New DNA strands are synthesized by Taq polymerase"], key="q4")
if q4 == "New DNA strands are synthesized by Taq polymerase":
    st.success("✅ Correct!")
elif q4:
    st.error("❌ That's not correct. Extension builds new DNA.")

st.info("📈 More levels, scoring, and progress tracking coming soon!")
elif topic:
    st.warning(f"No visual learning module available yet for: {topic}")
    st.info("✨ Try typing 'PCR' to see the full experience. More topics coming soon!")

# Footer
st.markdown("---")
st.caption("Built with 💡 by StudyMuse team")
