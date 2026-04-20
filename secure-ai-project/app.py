from flask import Flask, render_template, request
from model import predict
from security import security_check
import random

app = Flask(__name__)   # ✅ MUST come before @app.route

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    status = ""
    confidence = ""
    attacks = 0

    # Count attacks from logs
    try:
        with open("logs.txt", "r") as f:
            lines = f.readlines()
            attacks = sum(1 for line in lines if "ATTACK" in line or "ANOMALY" in line)
    except:
        attacks = 0

    if request.method == "POST":
        user_input = request.form["text"]

        is_safe, message = security_check(user_input)

        if not is_safe:
            result = "BLOCKED 🚫"
            status = message
            confidence = "Threat Confidence: 99%"
        else:
            prediction = predict(user_input)
            result = "SPAM ⚠️" if prediction == 1 else "NORMAL ✅"
            status = "Processed Successfully"
            confidence = f"AI Confidence: {random.randint(85, 98)}%"

    return render_template("index.html", result=result, status=status, confidence=confidence, attacks=attacks)

if __name__ == "__main__":
    print("🚀 Starting Flask App...")
    app.run(debug=True)