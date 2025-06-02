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
    topic = st.text_input("Enter a topic (e.g., PCR, CRISPR, Photosynthesis)")

    if topic:
        st.success(f"Results for: **{topic}**")
        st.markdown("### 🎥 Video Guide:")
        st.video("https://www.youtube.com/watch?v=2pp17E4E-O8")

        st.markdown("### 🧬 Visual Diagram:")
        st.image("https://upload.wikimedia.org/wikipedia/commons/5/5a/Polymerase_chain_reaction.svg", caption="Example PCR Diagram")

        st.info("🧠 Soon: Dynamic visual + video results via AI + YouTube API!")

st.markdown("---")
st.caption("Built with 💡 by StudyMuse team")


