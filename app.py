import streamlit as st
import json
from metadata_generator import (
    extract_text_from_txt,
    extract_text_from_docx,
    extract_text_from_pdf,
    extract_text_from_scanned_pdf,
    generate_metadata
)

st.set_page_config(page_title=" Metadata Generator", layout="wide")
st.title(" Automated Metadata Generator")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if uploaded_file:
    filetype = uploaded_file.type.split("/")[-1]
    filename = uploaded_file.name
    text = ""

    try:
        if filetype == "plain":
            text = extract_text_from_txt(uploaded_file)
        elif filetype == "vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = extract_text_from_docx(uploaded_file)
        elif filetype == "pdf":
            try:
                text = extract_text_from_pdf(uploaded_file)
            except:
                st.warning("Standard extraction failed, using OCR...")
                text = extract_text_from_scanned_pdf(uploaded_file.name)
        else:
            st.error("Unsupported file type")
            st.stop()
    except Exception as e:
        st.error(f"Error while processing the file: {e}")
        st.stop()

    st.subheader(" Extracted Text (First 3000 characters)")
    st.text_area("Extracted Text", text[:3000], height=300)

    metadata = generate_metadata(text, filename, filetype)

    st.subheader(" Generated Metadata")
    st.json(metadata)

    st.download_button(
        label=" Download Metadata as JSON",
        data=json.dumps(metadata, indent=2),
        file_name="metadata.json",
        mime="application/json"
    )
