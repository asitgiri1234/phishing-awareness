import joblib
from pathlib import Path
from preprocessor import clean_text

# Load model and vectorizer
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"

model = joblib.load(MODEL_DIR / "phishing_model.pkl")
tfidf = joblib.load(MODEL_DIR / "tfidf_vectorizer.pkl")


def predict_email(text):
    """
    Predict whether an email is phishing or safe
    """
    cleaned_text = clean_text(text)
    vectorized_text = tfidf.transform([cleaned_text])
    prediction = model.predict(vectorized_text)[0]

    if prediction == 1:
        return "Phishing Email"
    else:
        return "Safe Email"
if __name__ == "__main__":
    test_email = "Your account will be suspended. Verify immediately."
    print(predict_email(test_email))
