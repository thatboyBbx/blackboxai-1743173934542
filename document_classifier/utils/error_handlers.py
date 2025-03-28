class InvalidFileError(Exception):
    """Raised when an invalid file is uploaded"""
    def __init__(self, file_path, message="Invalid document file"):
        self.file_path = file_path
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.file_path}"

class ModelNotTrainedError(Exception):
    """Raised when trying to predict without training"""
    def __init__(self, message="Model has not been trained yet"):
        self.message = message
        super().__init__(self.message)

class TextExtractionError(Exception):
    """Raised when text extraction from document fails"""
    def __init__(self, file_path, message="Failed to extract text from document"):
        self.file_path = file_path
        self.message = message
        super().__init__(self.message)