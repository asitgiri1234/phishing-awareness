from pathlib import Path
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

from preprocessor import load_and_preprocess_data

# -----------------------------
# Load and preprocess data
# -----------------------------
df = load_and_preprocess_data()

X = df['text']
y = df['label']

# -----------------------------
# Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------
# TF-IDF Vectorization
# -----------------------------
tfidf = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

# -----------------------------
# Models
# -----------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Support Vector Machine": LinearSVC(),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = {}

# -----------------------------
# Train & Evaluate
# -----------------------------
for name, model in models.items():
    print(f"\nTraining {name}...")
    model.fit(X_train_tfidf, y_train)

    y_pred = model.predict(X_test_tfidf)

    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    results[name] = accuracy

    print(f"{name} Accuracy: {accuracy:.4f}")
    print(report)

# -----------------------------
# Select best model
# -----------------------------
best_model_name = max(results, key=results.get)
best_model = models[best_model_name]

print(f"\nBest Model: {best_model_name}")

# -----------------------------
# Save best model & TF-IDF
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

joblib.dump(best_model, MODEL_DIR / "phishing_model.pkl")
joblib.dump(tfidf, MODEL_DIR / "tfidf_vectorizer.pkl")

print("\nBest model and TF-IDF vectorizer saved successfully.")
