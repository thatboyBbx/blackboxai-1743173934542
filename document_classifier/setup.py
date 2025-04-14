from setuptools import setup, find_packages

setup(
    name="document_classifier",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'scikit-learn==1.0.2',
        'pandas==1.3.5',
        'numpy==1.21.6',
        'python-magic==0.4.27',
        'joblib==1.2.0',
        'PyPDF2==3.0.1',
        'python-docx==0.8.11',
        'openpyxl==3.0.10',
        'python-pptx==0.6.21'
    ],
)