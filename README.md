Real-Time Phishing Awareness System Using NLP

Overview

PhishGuard is a lightweight and extensible phishing detection system designed to analyze text-based messages and classify them as phishing or legitimate. The system focuses on improving user awareness by identifying potentially malicious content in real time.

This repository contains the Phase-1 implementation, which establishes the foundational pipeline, including preprocessing, basic classification logic, and a minimal web interface.

The project is designed with scalability in mind, allowing seamless integration of advanced machine learning models and real-time APIs in future phases.

Features

Text preprocessing pipeline for cleaning and normalizing input data

Rule-based or placeholder model for phishing classification

Simple and interactive Flask-based web interface

Modular and extensible architecture for future ML integration

Lightweight implementation suitable for rapid prototyping

Project Structure
PhishGuard/
│
├── app.py                 # Flask application entry point
├── model/
│   └── model.py           # Placeholder / dummy model logic
├── preprocessing/
│   └── preprocess.py      # Text preprocessing pipeline
├── templates/
│   └── index.html         # Frontend UI
├── static/                # CSS/JS assets (if any)
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
How It Works

User inputs a message through the web interface

The message is processed using a preprocessing pipeline (cleaning, normalization, etc.)

The processed text is passed to the classification module

The system returns a prediction: Phishing or Legitimate

Installation
Prerequisites

Python 3.8 or higher

pip package manager

Setup Steps
# Clone the repository
git clone https://github.com/your-username/phishguard.git

# Navigate into the project directory
cd phishguard

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
Usage

Open your browser and go to: http://127.0.0.1:5000/

Enter a message in the input field

Submit the message to receive a classification result

Current Limitations

Uses a placeholder or rule-based model instead of a trained ML model

Limited dataset and feature engineering

No real-time API integration yet

Basic preprocessing without advanced NLP techniques

Future Enhancements

Integration of TF-IDF vectorization

Implementation of Logistic Regression and Support Vector Machine models

Deployment of a real-time detection API

Advanced preprocessing (stopword removal, stemming, lemmatization)

Explainable AI features for prediction transparency

Model evaluation metrics (accuracy, precision, recall, F1-score)

Tech Stack

Python

Flask

Natural Language Processing (NLP)

Scikit-learn (planned)
