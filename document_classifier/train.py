import argparse
from document_classifier.classifier import DocumentClassifier
import pandas as pd

def main():
    parser = argparse.ArgumentParser(description='Train document classifier')
    parser.add_argument('dataset', help='Path to training dataset CSV')
    parser.add_argument('--save', default='models', help='Model save directory')
    args = parser.parse_args()

    print(f"Training classifier using dataset: {args.dataset}")
    
    # Initialize and train classifier
    classifier = DocumentClassifier()
    if classifier.train(args.dataset, args.save):
        print("Training completed successfully")
        print(f"Model saved to: {args.save}")
    else:
        print("Training failed")

if __name__ == '__main__':
    main()