import PyPDF2
import docx
from .error_handlers import TextExtractionError

def extract_text_from_pdf(file_path):
    """Extract text from PDF files"""
    try:
        text = ""
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        raise TextExtractionError(file_path, f"PDF extraction failed: {str(e)}")

def extract_text_from_docx(file_path):
    """Extract text from DOCX files"""
    try:
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    except Exception as e:
        raise TextExtractionError(file_path, f"DOCX extraction failed: {str(e)}")

def get_document_text(file_path):
    """Main text extraction interface"""
    if file_path.endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        return extract_text_from_docx(file_path)
    elif file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise TextExtractionError(file_path, "Unsupported file format")