import os
import magic
from pathlib import Path

def validate_file(file_path):
    """Validate if file is a work document"""
    allowed_mime_types = [
        'application/pdf',
        'application/msword',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'text/plain'
    ]
    
    # Check file extension
    valid_extensions = ('.pdf', '.doc', '.docx', '.txt')
    if not file_path.lower().endswith(valid_extensions):
        return False
    
    # Check MIME type
    mime = magic.Magic(mime=True)
    file_mime = mime.from_file(file_path)
    
    if file_mime not in allowed_mime_types:
        return False
    
    return True

def create_category_folder(category):
    """Create folder for document category if it doesn't exist"""
    path = Path(f"classified_docs/{category}")
    path.mkdir(exist_ok=True, parents=True)
    return path

def get_document_text(file_path):
    """Extract text from supported document types"""
    # TODO: Implement text extraction for PDF/DOCX
    # For now just handles text files
    if file_path.endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""