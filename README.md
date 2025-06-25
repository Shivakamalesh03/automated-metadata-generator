
# Automated Metadata Generator

The Automated Metadata Generator is a lightweight web application that extracts structured metadata from unstructured documents (PDF, DOCX, TXT). It helps users quickly understand a document by generating its title, summary, keywords, and named entities, along with language and file-level information.

## Features

- **Title Detection**: Extracts a clean, contextually relevant title from the document.
- **Summary Generation**: Uses a transformer-based NLP model to generate a short, readable summary.
- **Keyword Extraction**: Identifies the top keywords based on word frequency, excluding stopwords.
- **Named Entity Recognition (NER)**: Detects people, organizations, places, and dates.
- **Language Detection**: Automatically identifies the document's language.
- **Text Extraction**: Handles standard and scanned PDFs, DOCX, and TXT formats.
- **Web Interface**: Intuitive UI built with Streamlit for ease of use.

## Technology Stack Used

- **Streamlit** – UI and interaction
- **spaCy** – Named Entity Recognition
- **Transformers (Hugging Face)** – Text summarization
- **PyMuPDF + pytesseract** – PDF parsing and OCR
- **scikit-learn** – Keyword filtering
- **langdetect** – Language detection
- **Python 3.10** – Backend
- 
## Installation

1. Clone the repository:
### 1. Clone the repository

```bash
git clone https://github.com/Shivakamalesh03/automated-metadata-generator.git
cd automated-metadata-generator

2.Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

3. Install the required packages:
pip install --upgrade pip
pip install -r requirements.txt

4.Run the app
streamlit run app.py

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
