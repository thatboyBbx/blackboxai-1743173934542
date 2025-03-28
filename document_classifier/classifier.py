import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
from document_classifier.utils.text_extraction import get_document_text
from document_classifier.utils.error_handlers import ModelNotTrainedError

class DocumentClassifier:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,3))
        self.model = LogisticRegression(class_weight='balanced',
                                      max_iter=1000,
                                      C=0.1,
                                      solver='liblinear')
        self.is_trained = False
        self.classes_ = None

    def train(self, dataset_path, save_path='document_classifier/models'):
        """Train classifier on dataset and save model"""
        try:
            # Load and prepare dataset
            data = pd.read_csv(dataset_path)
            X = data['text'].values
            y = data['category'].values
            
            # Vectorize text
            X_vectorized = self.vectorizer.fit_transform(X)
            self.classes_ = list(set(y))

            # Split data
            X_train, X_test, y_train, y_test = train_test_split(
                X_vectorized, y, test_size=0.2, random_state=42
            )

            # Train model
            self.model.fit(X_train, y_train)
            self.is_trained = True

            # Evaluate
            y_pred = self.model.predict(X_test)
            print(classification_report(y_test, y_pred))

            # Save model
            os.makedirs(save_path, exist_ok=True)
            joblib.dump(self.model, f'{save_path}/model.pkl')
            joblib.dump(self.vectorizer, f'{save_path}/vectorizer.pkl')
            joblib.dump(self.classes_, f'{save_path}/classes.pkl')

            return True
        except Exception as e:
            print(f"Training failed: {str(e)}")
            return False

    def predict(self, document_path):
        """Predict document category"""
        if not self.is_trained:
            raise ModelNotTrainedError()

        try:
            # Extract text
            content = get_document_text(document_path)
            
            # Vectorize and predict
            content_vectorized = self.vectorizer.transform([content])
            return self.model.predict(content_vectorized)[0]
        except Exception as e:
            raise Exception(f"Prediction failed: {str(e)}")

    def load_model(self, model_path='document_classifier/models'):
        """Load pre-trained model"""
        try:
            self.model = joblib.load(f'{model_path}/model.pkl')
            self.vectorizer = joblib.load(f'{model_path}/vectorizer.pkl')
            self.classes_ = joblib.load(f'{model_path}/classes.pkl')
            self.is_trained = True
            return True
        except Exception as e:
            print(f"Failed to load model: {str(e)}")
            return False
