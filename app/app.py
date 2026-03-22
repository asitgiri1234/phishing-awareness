from flask import Flask, render_template, request
import sys
from pathlib import Path

# Allow app to access src folder
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "src"))

from infer import predict_email

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        email_text = request.form["email_text"]
        prediction = predict_email(email_text)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
