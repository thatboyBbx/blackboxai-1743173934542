import os
from utils.file_utils import validate_file
from utils.text_extraction import get_document_text

def test_office_support():
    # Test file validation
    test_files = {
        'docx': 'test_samples/sample.docx',
        'xlsx': 'test_samples/sample.xlsx', 
        'pptx': 'test_samples/sample.pptx'
    }
    
    print("Testing Office file support:")
    for file_type, file_path in test_files.items():
        if os.path.exists(file_path):
            print(f"\nValidating {file_type.upper()} file:")
            print(f"Validation result: {validate_file(file_path)}")
            
            print(f"\nExtracting text from {file_type.upper()} file:")
            try:
                text = get_document_text(file_path)
                print(f"Extracted text length: {len(text)} characters")
                print(f"First 100 chars: {text[:100]}...")
            except Exception as e:
                print(f"Error extracting text: {str(e)}")
        else:
            print(f"\nTest file not found: {file_path}")

if __name__ == "__main__":
    test_office_support()