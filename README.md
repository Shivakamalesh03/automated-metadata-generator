# Automated Metadata Generation System

This project helps you automatically generate useful metadata from your documents. It works with PDFs, Word files (DOCX), and plain text files. Even if the document is scanned (like an image-based PDF), the system can extract the text using OCR. Everything runs in a simple Streamlit web app.

---

## Features

- Upload and process PDF, DOCX, and TXT files
- OCR support for scanned PDFs using Tesseract
- Generates metadata like:
  - Title
  - Summary
  - Keywords
  - Word and character counts
  - Language detection
  - Named entities (people, organizations, etc.)
- Built-in NLP models for summarization (using HuggingFace Transformers)
- Clean Streamlit interface to upload files and view metadata
- Download results as a JSON file

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **NLP & Text Processing:**  
  - HuggingFace Transformers (T5-small)  
  - spaCy (NER)  
  - langdetect  
- **OCR:** pytesseract  
- **PDF Parsing:** PyMuPDF, pdf2image  
- **DOCX Handling:** python-docx

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Shivakamalesh03/automated-metadata-generator.git
cd automated-metadata-generator
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. (Optional) Add `tesseract` to your system path if it's not already installed.

4. Run the app:

```bash
streamlit run app.py
```

---

## Deployment

The app is ready to be deployed on Streamlit Cloud. It uses a `requirements.txt` and `runtime.txt` to ensure the correct Python environment and dependencies.

---

## Folder Structure

```
├── app.py                      # Main Streamlit app
├── metadata_generator.py       # Core logic for parsing and metadata generation
├── metadata_generator.ipynb    # Notebook version for local experimentation
├── requirements.txt
├── runtime.txt
├── README.md
```

---

## Sample Output

Once you upload a document, the app shows:
- Extracted text (first few thousand characters)
- Clean JSON metadata you can download


## Contact

Created by [Shivakamalesh03](https://github.com/Shivakamalesh03)