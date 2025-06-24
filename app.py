import streamlit as st
import json
import os
import tempfile
from metadata_generator import (
    extract_text_from_txt,
    extract_text_from_docx,
    extract_text_from_pdf,
    extract_text_from_scanned_pdf,
    generate_metadata
)

st.set_page_config(page_title="Metadata Generator", layout="wide")
st.title("Automated Metadata Generator")

st.sidebar.title("About")
st.sidebar.markdown("""
This app extracts useful metadata from uploaded documents (PDF, DOCX, TXT).  
It generates:
- Title  
- Summary  
- Keywords  
- Named Entities  
- Language and file info  
""")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if uploaded_file:
    filetype = uploaded_file.type.split("/")[-1]
    filename = uploaded_file.name
    text = ""
    page_count = None

    with st.spinner("Extracting content..."):
        try:
            if filetype == "plain":
                text = extract_text_from_txt(uploaded_file)
            elif filetype == "vnd.openxmlformats-officedocument.wordprocessingml.document":
                text = extract_text_from_docx(uploaded_file)
            elif filetype == "pdf":
                try:
                    text = extract_text_from_pdf(uploaded_file)
                except:
                    st.warning("Standard PDF extraction failed. Trying OCR fallback...")
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                        tmp_file.write(uploaded_file.read())
                        tmp_file_path = tmp_file.name
                    text = extract_text_from_scanned_pdf(tmp_file_path)
                    os.remove(tmp_file_path)
            else:
                st.error("Unsupported file type.")
                st.stop()
        except Exception as e:
            st.error(f"Error reading file: {e}")
            st.stop()

    st.subheader("Extracted Text (First 3000 characters)")
    st.text_area("Preview", text[:3000], height=300)

    with st.spinner("Generating metadata..."):
        metadata = generate_metadata(text, filename, filetype, page_count)

    st.subheader("Generated Metadata")
    st.json(metadata, expanded=False)

    st.markdown("### Title")
    st.write(metadata.get("title", "Not available"))

    st.markdown("### Summary")
    st.info(metadata.get("summary", "Summary not available"))

    st.markdown("### Keywords")
    st.write(", ".join(metadata.get("keywords", [])))

    st.markdown("### Named Entities")
    for ent in metadata.get("named_entities", []):
        st.markdown(f"- {ent}")

    st.download_button(
        label="Download Metadata as JSON",
        data=json.dumps(metadata, indent=2),
        file_name="metadata.json",
        mime="application/json"
    )
