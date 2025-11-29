# src/infer.py
import random
from src.preprocessor import basic_clean

def predict_basic(text):
    clean = basic_clean(text)

    # Mock prediction for now
    prediction = random.choice(["phishing", "legitimate"])

    return prediction


if __name__ == "__main__":
    txt = input("Enter message: ")
    result = predict_basic(txt)
    print("Prediction:", result)
