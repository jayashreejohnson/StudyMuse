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
            **Polymerase Chain Reaction (PCR)** is a revolutionary molecular biology technique used to selectively amplify DNA. It enables researchers to create millions of copies of a specific DNA segment from a minimal starting amount. This exponential amplification is achieved through repeated cycles of thermal processing — mimicking natural DNA replication in a test tube.

            #### 🔬 Why is PCR Important?
            PCR transformed modern science by:
            - Making **DNA analysis faster, cheaper, and accessible**
            - Enabling **genetic testing** without needing large tissue samples
            - Powering techniques in **genomics, diagnostics, forensics, and research**

            #### 🧪 Core Principle
            PCR mimics natural DNA replication but is controlled artificially using a **thermal cycler** and a **heat-stable DNA polymerase** (Taq polymerase). Each cycle **doubles** the DNA target — leading to over a billion copies in under 30 cycles.

            #### ⚙️ Components Required
            - **Template DNA**: the target sequence you want to amplify
            - **Primers**: short synthetic DNA pieces that flank the target
            - **Taq Polymerase**: derived from *Thermus aquaticus*, can withstand high heat
            - **dNTPs**: free nucleotides (A, T, G, C) used to build new strands
            - **Buffer + MgCl₂**: ensures enzyme activity and reaction stability

            #### 🔁 Step-by-Step Workflow
            1. **Denaturation (94–96°C)**  
               DNA is heated to break hydrogen bonds and separate the strands.
            2. **Annealing (50–65°C)**  
               Primers attach to complementary sequences on each strand.
            3. **Extension (72°C)**  
               Taq polymerase adds nucleotides to build the new DNA strands.

            This 3-step process is repeated ~30 times, resulting in exponential amplification.

            #### 🏆 Historical Significance
            - Invented by **Kary Mullis** in 1983 during a drive along the California coast.
            - Awarded the **1993 Nobel Prize in Chemistry** for PCR’s profound scientific impact.

            #### 🚀 Limitations
            - Highly sensitive to contamination  
            - Requires prior knowledge of flanking sequences for primer design  
            - Not suitable for amplifying extremely long DNA fragments
            """)

            # --- Applications ---
            st.markdown("### 💡 Applications of PCR")
            st.markdown("""
            - 🧪 Medical diagnostics (COVID-19, HIV, etc.)
            - 🔬 Forensic DNA fingerprinting
            - 🧬 Mutation detection in genetic testing
            - 🌿 Detection of GMOs in crops
            - 🧫 Gene expression and cloning in research
            """)

            # --- Diagrams ---
            st.markdown("### 🖼️ Visual Diagrams")
            st.image("https://upload.wikimedia.org/wikipedia/commons/8/86/PCR.png", caption="PCR Cycle", use_container_width=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/f/f5/PCR_steps.png", caption="PCR Steps", use_container_width=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/4/4c/Components_of_a_PCR.png", caption="PCR Components", use_container_width=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/0/09/Thermal_cycler.png", caption="Thermal Cycler", use_container_width=True)
            st.image("https://upload.wikimedia.org/wikipedia/commons/5/54/Taq-polymerase.png", caption="Taq Polymerase", use_container_width=True)

            # --- Videos ---
            st.markdown("### 🎥 Watch & Learn")
            st.video("https://www.youtube.com/embed/2KoLnIwoZKU")
            st.video("https://www.youtube.com/embed/_YgXcJ4n-kQ")
            st.video("https://www.youtube.com/embed/ON2BtjL-8wM")

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

