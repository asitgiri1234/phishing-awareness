import pandas as pd
import re
import nltk
from pathlib import Path
from nltk.corpus import stopwords

# Download stopwords (runs once, cached later)
nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = text.split()
    words = [word for word in words if word not in STOP_WORDS]
    return ' '.join(words)


def load_and_preprocess_data():
    """
    Load dataset, preprocess text, encode labels
    """
    # Get absolute path to data file (SAFE METHOD)
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "data" / "Phishing_Email.csv"

    df = pd.read_csv(DATA_PATH)

    # Drop unnecessary index column
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    # Rename columns
    df.columns = ['text', 'label']

    # Encode labels
    df['label'] = df['label'].map({
        'Phishing Email': 1,
        'Safe Email': 0
    })

    # Clean text
    df['text'] = df['text'].apply(clean_text)

    return df


# -----------------------------
# Standalone test
# -----------------------------
if __name__ == "__main__":
    df = load_and_preprocess_data()

    print("Dataset shape:", df.shape)
    print("\nSample rows:")
    print(df.head())

    print("\nLabel distribution:")
    print(df['label'].value_counts())
