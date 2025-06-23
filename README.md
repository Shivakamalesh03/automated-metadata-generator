# Automated Metadata Generation System

This project automatically generates structured metadata for unstructured documents (PDF, DOCX, TXT) using NLP techniques and a user-friendly web interface.

---

## Features

-  Supports PDF, DOCX, and TXT
-  OCR for scanned PDFs
-  Extracts Title, Summary, Keywords, Language, and more
-  Summarization via Transformer-based NLP models
-  Streamlit web interface for upload and viewing
-  Export metadata as JSON
-  Named Entity Recognition (NER) for advanced tagging

---

##  Tech Stack

- Frontend: Streamlit
- Backend: Python
- NLP: HuggingFace Transformers, spaCy, langdetect
- OCR: pytesseract
- PDF Parsing: PyMuPDF, pdf2image
- DOCX: python-docx

---

##  Installation

```bash
git clone https://github.com/your-username/automated-metadata-generator.git
cd automated-metadata-generator
pip install -r requirements.txt
