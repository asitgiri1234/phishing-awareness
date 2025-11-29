# src/train.py
import pandas as pd
from src.preprocessor import basic_clean

def load_data(path="../data/emails.csv"):
    df = pd.read_csv(path)
    return df

def train_basic():
    df = load_data()
    df["cleaned"] = df["text"].apply(basic_clean)
    print("Training placeholder completed.")
    print("Total rows processed:", len(df))

if __name__ == "__main__":
    train_basic()
