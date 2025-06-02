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
        st.success("🧬 Visual Learning Experience for: PCR")

        # --- Section 1: Interactive Video ---
        st.markdown("### 🎥 Interactive Video")
        st.video("https://www.youtube.com/watch?v=2pp17E4E-O8")
        st.markdown("**Topic:** What is PCR? | Source: DNA Learning Center")

        # --- Section 2: PCR Components Breakdown ---
        st.markdown("### 🧩 PCR Reaction Components")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🧬 Template DNA")
            st.markdown("- Sequence to amplify\n- Can be plasmid or genomic\n- Must contain binding sites")

            st.markdown("#### 🧪 Taq Polymerase")
            st.markdown("- Heat-stable enzyme\n- Builds new DNA strands")

        with col2:
            st.markdown("#### 🧲 Primers (F/R)")
            st.markdown("- Forward + Reverse primers\n- 18–25 bases long\n- Define target region")

            st.markdown("#### 🧬 dNTPs")
            st.markdown("- Nucleotide building blocks\n- A, T, G, C for extension")

        # --- Section 3: PCR 3-Step Mechanism ---
        st.markdown("### 🔄 PCR Three-Step Process")

        st.markdown("#### 🥵 Step 1: Denaturation (94–96°C)")
        st.markdown("- Heat breaks H-bonds\n- dsDNA → ssDNA")

        st.markdown("#### ❄️ Step 2: Annealing (50–65°C)")
        st.markdown("- Primers bind target sequences")

        st.markdown("#### 🔧 Step 3: Extension (72°C)")
        st.markdown("- Taq Polymerase extends new DNA strand")

        # --- Section 4: Mini Quiz Placeholder ---
        st.markdown("### 🧠 Quick Quiz")
        st.markdown("> **Q: What does PCR stand for?**")
        st.radio("Choose an answer:", ["Protein Chain Reaction", "Polymerase Chain Reaction", "Primer Copy Replication"], index=None)

        st.info("📌 Scoring, feedback & progress tracking coming soon!")

    else:
        st.warning("Try typing: `PCR` to explore full visual learning experience.")
        st.info("✨ Soon: More topics like miRNA, CRISPR, RNAi and others will be added here!")

# Footer
st.markdown("---")
st.caption("Made with 💡 by StudyMuse team")


