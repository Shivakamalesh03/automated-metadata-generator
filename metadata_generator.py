import os
import json
import pytesseract
import docx
import fitz  # PyMuPDF
from PIL import Image
from pdf2image import convert_from_path
from datetime import datetime
from transformers import pipeline
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import langdetect
import uuid
import spacy

# Load models
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
nlp = spacy.load("en_core_web_sm")

# --- Text Extraction Functions ---
def extract_text_from_txt(file):
    return file.read().decode("utf-8")

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_pdf(file):
    text = ""
    doc = fitz.open(stream=file.read(), filetype="pdf")
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_scanned_pdf(file_path):
    images = convert_from_path(file_path)
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

# --- Metadata Generation ---
def generate_metadata(text, filename, filetype, page_count=None):
    words = text.split()
    lines = text.strip().split("\n")

    title = next((line.strip() for line in lines if len(line.strip()) > 10), filename)
    if len(title) > 80:
        title = title[:77] + "..."

    try:
        summary = summarizer(text[:1000], max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    except:
        summary = " ".join(words[:40]) + ("..." if len(words) > 40 else "")
    summary = summary.strip()

    cleaned_words = [word.lower().strip(".,()[]{}\":'") for word in words if len(word) > 4 and word.lower() not in ENGLISH_STOP_WORDS]
    freq_keywords = [word for word, count in Counter(cleaned_words).most_common(15)]
    keywords = list(dict.fromkeys(freq_keywords))[:10]

    try:
        language = langdetect.detect(text[:1000])
    except:
        language = "unknown"

    doc = nlp(text[:1000])
    named_entities = list(set([ent.text for ent in doc.ents if len(ent.text.strip()) > 3]))

    metadata = {
        "document_id": str(uuid.uuid4()),
        "title": title,
        "summary": summary,
        "keywords": keywords,
        "file_type": filetype,
        "character_count": len(text),
        "word_count": len(words),
        "uploaded_on": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "filename": filename,
        "language": language,
        "named_entities": named_entities
    }

    if page_count:
        metadata["page_count"] = page_count

    return metadata
