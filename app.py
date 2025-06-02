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
        st.markdown("- Invented by **Kary Mullis** in 1983\n- Awarded the **Nobel Prize in Chemistry (1993)**")

        # --- Applications ---
        st.markdown("### 💡 Applications of PCR")
        st.markdown("""
        - 🧪 Diagnosing infectious diseases (e.g., COVID-19)
        - 🧬 Gene expression analysis
        - 🔬 DNA fingerprinting
        - 🌱 GMO detection
        - 🧫 Cancer mutation detection
        """)

        # --- Components ---
        st.markdown("### 🔧 PCR Components")
        st.markdown("""
        - **Template DNA** – the target DNA
        - **Primers** – short DNA sequences
        - **Taq Polymerase** – heat-stable enzyme
        - **dNTPs** – nucleotide mix
        - **Mg²⁺ and buffer** – for enzyme activity
        """)

        # --- Mechanism ---
        st.markdown("### 🔄 3-Step PCR Cycle")
        st.markdown("""
        1. **Denaturation (94–96°C)** – strands separate  
        2. **Annealing (50–65°C)** – primers bind  
        3. **Extension (72°C)** – new strands built
        """)

        # --- Videos ---
        st.markdown("### 🎥 Learn Visually")
        st.video("https://www.youtube.com/watch?v=2KoLnIwoZKU")
        st.video("https://www.youtube.com/watch?v=_YgXcJ4n-kQ")
        st.video("https://www.youtube.com/watch?v=3t-Nm4qAC8M")

        # --- Diagrams ---
        st.markdown("### 🖼️ Diagrams")
        st.image("https://i.imgur.com/nZB9QyM.png", caption="PCR Flow Overview")
        st.image("https://i.imgur.com/w3VFIcy.png", caption="3-Step Cycle")
        st.image("https://i.imgur.com/9v6FzAW.png", caption="PCR Setup")
        st.image("https://i.imgur.com/UmcMbv1.png", caption="Amplification Rounds")
        st.image("https://i.imgur.com/6pSFXbP.png", caption="Taq Polymerase Function")

        # --- Quizzes ---
        st.markdown("### 🧠 Quiz Time")

        q1 = st.radio("1. What does PCR stand for?", 
                      ["Protein Chain Reaction", "Polymerase Chain Reaction", "Primer Cloning Reaction"], key="q1")
        if q1 == "Polymerase Chain Reaction":
            st.success("✅ Correct!")
        elif q1:
            st.error("❌ It's Polymerase Chain Reaction.")

        q2 = st.radio("2. What enzyme is used?", 
                      ["DNA Ligase", "RNA Polymerase", "Taq Polymerase"], key="q2")
        if q2 == "Taq Polymerase":
            st.success("✅ Correct!")
        elif q2:
            st.error("❌ It's Taq Polymerase.")

        q3 = st.radio("3. At what temp does annealing occur?", 
                      ["30–40°C", "50–65°C", "75–85°C"], key="q3")
        if q3 == "50–65°C":
            st.success("✅ Correct!")
        elif q3:
            st.error("❌ It’s around 50–65°C.")

        q4 = st.radio("4. What happens during extension?", 
                      ["DNA separates", "Primers bind", "Taq builds DNA"], key="q4")
        if q4 == "Taq builds DNA":
            st.success("✅ Correct!")
        elif q4:
            st.error("❌ Taq builds the new DNA strands.")

        st.info("📈 Scoring, difficulty levels, and progress tracking coming soon!")

    elif topic:
        st.warning(f"No visual learning module available yet for: {topic}")
        st.info("✨ Try typing 'PCR' to see a complete example.")

# Footer
st.markdown("---")
st.caption("Built with 💡 by StudyMuse team")

