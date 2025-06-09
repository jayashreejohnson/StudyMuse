import streamlit as st
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import tempfile
import time

# --- Page config ---
st.set_page_config(page_title="StudyMuse", layout="centered")

# --- Custom Pastel Theme ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffeef2 0%, #fdf6f0 50%, #eef9ff 100%);
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stTabs [data-baseweb="tab-list"] {
        background-color: #fce6ec;
        border-radius: 12px;
        padding: 5px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #ffd6e6 !important;
        border-radius: 8px;
        color: #000 !important;
        font-weight: bold;
    }
    .stTextInput > div > div > input {
        background-color: #fff0f5;
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #f9c3d1;
    }
    .stAlert-success {
        background-color: #e6fffa;
        color: #26d4a4;
    }
    h1, h2, h3, h4 {
        color: #3f3f3f;
    }
    .stMarkdown {
        color: #2f2f2f;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📚 StudyMuse – Visual Memory Aid for Science Students")

tab1, tab2 = st.tabs(["📤 Upload Notes", "🔍 Search Topic"])

# --- Upload Notes Tab ---
with tab1:
    st.subheader("Upload notes (PDF or image)")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "png", "jpg", "jpeg"])

    if uploaded_file:
        file_type = uploaded_file.type
        if "pdf" in file_type:
            with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
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

# --- Search Topic Tab ---
with tab2:
    st.subheader("Search Biotech/Science Topic")
    topic = st.text_input("Enter a topic (e.g., PCR, miRNA, CRISPR)")

    if topic.lower() == "pcr":
        with st.spinner("✨ Summoning your visual memory experience..."):
            time.sleep(1.5)
        st.balloons()
        st.success("🧬 Learning Module: Polymerase Chain Reaction (PCR)")

        st.markdown("### 📋 What is PCR?")
        st.markdown("PCR (Polymerase Chain Reaction) is a revolutionary method used to amplify small DNA fragments into millions of copies, enabling deep biological analysis from minute samples.")

        with st.expander("📌 Important Points about PCR"):
            st.markdown("""
- 🧬 Rapid DNA amplification technique  
- 🧪 Uses primers, nucleotides, polymerase, and template DNA  
- 🔥 Involves thermal cycling (heat → cool → extend)  
- 👨‍🔬 Invented by Kary Mullis (Nobel Prize, 1993)  
- 🧫 Widely used in diagnostics, cloning, forensics, and research  
""")

        st.markdown("### 🧩 Components of PCR")
        st.markdown("""
- **DNA Template** – the sequence to be copied  
- **Primers** – short synthetic DNA strands flanking the region of interest  
- **Taq Polymerase** – heat-stable enzyme from *Thermus aquaticus*  
- **dNTPs** – nucleotides (A, T, G, C) to build new strands  
- **Buffer Solution** – maintains optimal pH  
- **Mg²⁺ Ions** – essential cofactor for enzyme function  
""")

        st.markdown("### 🔁 Steps in PCR Cycle")
        st.markdown("""
1. **Denaturation (94–96°C)**: DNA strands separate  
2. **Annealing (50–65°C)**: Primers bind to target regions  
3. **Extension (72°C)**: Taq polymerase adds nucleotides  
🔁 Repeated for 30–40 cycles to amplify DNA
""")

        st.markdown("### 🧪 Applications of PCR")
        st.markdown("""
- **Medical diagnostics** (e.g. COVID-19, HIV, genetic mutations)  
- **Forensics** – DNA fingerprinting from trace evidence  
- **Research** – Gene cloning, sequencing prep, mutagenesis  
- **Agricultural biotech** – GMO detection, plant disease diagnosis  
- **Environmental** – Microbial and pathogen detection in samples  
""")

        st.markdown("### 💼 Career Opportunities Involving PCR")
        st.markdown("""
- 🧬 **Molecular Biologist** – gene editing, cloning, expression studies  
- 🔬 **Clinical Lab Scientist** – pathogen detection, prenatal testing  
- 🕵️‍♀️ **Forensic Analyst** – crime scene DNA matching  
- 🧪 **Pharma QA/QC** – purity & contamination checks  
- 📈 **Bioinformatics Analyst** – analyze PCR & sequencing outputs  
""")

        st.markdown("### 📚 PCR Learning Resources")
        st.markdown("""
- 📺 [MIT PCR Tutorial](https://www.youtube.com/watch?v=2KoLnIwoZKU)  
- 📘 [Nature Education: PCR](https://www.nature.com/scitable/topicpage/pcr-technology-490/)  
- 🧪 [Addgene PCR Protocols](https://www.addgene.org/protocols/pcr/)  
- 🎓 [Coursera: Genomic Data Science](https://www.coursera.org/learn/genomic-data-science)  
""")

        st.markdown("### 🖼️ Visual Workflow of PCR")

        col1, col2 = st.columns(2)
        with col1:
            st.image("assets/pcr/PCR1.jpeg", caption="PCR Overview", use_column_width=True)
            st.image("assets/pcr/PCR2.jpg", caption="PCR Machine – Thermal Cycler", use_column_width=True)
            st.image("assets/pcr/PCR3.jpg", caption="Denaturation Step", use_column_width=True)
        with col2:
            st.image("assets/pcr/PCR4.png", caption="Annealing Step", use_column_width=True)
            st.image("assets/pcr/PCR5.jpeg", caption="Extension Step", use_column_width=True)

        with st.expander("✅ Advantages of PCR"):
            st.markdown("""
- Detects DNA from very low amounts  
- Fast turnaround time  
- Adaptable to many DNA/RNA types  
- Portable PCR kits now exist  
""")

        with st.expander("⚠️ Limitations of PCR"):
            st.markdown("""
- Sensitive to contamination  
- Requires prior sequence knowledge  
- Can’t distinguish live vs. dead DNA sources  
""")

        with st.expander("🎉 Fun Facts"):
            st.markdown("""
- PCR idea came to Kary Mullis on a road trip  
- Taq polymerase comes from a hot spring bacterium  
- PCR helped detect SARS-CoV-2 within days of outbreak  
""")

        st.markdown("### 🎥 Watch & Learn")
        st.video("https://www.youtube.com/watch?v=2KoLnIwoZKU")
        st.video("https://www.youtube.com/watch?v=_YgXcJ4n-kQ")
        st.video("https://www.youtube.com/watch?v=2aZ4YzGFOAo")

        st.markdown("### 🧠 Quick Quiz")

        q1 = st.radio("1. What enzyme is used in PCR?", 
                      ["DNA Ligase", "Taq Polymerase", "RNA Polymerase"], key="q1")
        if q1 == "Taq Polymerase":
            st.success("✅ Correct!")
        elif q1:
            st.error("❌ Nope. The correct answer is Taq Polymerase.")

        q2 = st.radio("2. What happens during denaturation?", 
                      ["Primers bind", "DNA strands separate", "Polymerase extends DNA"], key="q2")
        if q2 == "DNA strands separate":
            st.success("✅ That's right!")
        elif q2:
            st.error("❌ Denaturation splits the DNA strands.")

        q3 = st.radio("3. What temperature is optimal for extension?", 
                      ["37°C", "50°C", "72°C"], key="q3")
        if q3 == "72°C":
            st.success("✅ Correct!")
        elif q3:
            st.error("❌ Extension occurs around 72°C.")

        st.info("📈 More levels, points, and unlockable flashcards coming soon!")

    elif topic:
        st.warning(f"⚠️ No visual learning module yet for: {topic}")
        st.info("✨ Try typing 'PCR' to explore an interactive demo.")

