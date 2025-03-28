import os
from document_classifier.classifier import DocumentClassifier
from document_classifier.utils.file_utils import validate_file
from document_classifier.utils.error_handlers import InvalidFileError, ModelNotTrainedError

def test_classification():
    """Test the document classification workflow"""
    print("Initializing document classifier...")
    classifier = DocumentClassifier()
    
    # Try loading pre-trained model
    if not classifier.load_model('/project/sandbox/user-workspace/document_classifier/models'):
        print("Warning: No pre-trained model found. Please train first.")
        return

    # Test with sample documents
    test_files = [
        ("financial_report.txt", "Financial")
    ]

    print("\nRunning classification tests:")
    for filename, expected_category in test_files:
        filepath = os.path.join("document_classifier/test_samples", filename)
        
        if not os.path.exists(filepath):
            print(f"  [SKIP] Test file not found: {filepath}")
            continue

        try:
            # Validate and classify
            if not validate_file(filepath):
                raise InvalidFileError(filepath)
            
            predicted = classifier.predict(filepath)
            result = "PASSED" if predicted == expected_category else "FAILED"
            print(f"  {result} - {filename}: Predicted '{predicted}' (Expected: '{expected_category}')")
            
        except Exception as e:
            print(f"  ERROR - {filename}: {str(e)}")

if __name__ == '__main__':
    test_classification()