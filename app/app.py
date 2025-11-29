# app/app.py
from flask import Flask, render_template, request
from src.infer import predict_basic

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    
    if request.method == "POST":
        text = request.form.get("message", "")
        result = predict_basic(text)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
