from flask import Flask, request, jsonify, render_template_string
import os

app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template_string(open("index.html").read())

# Credit check API route
@app.route("/check-credit", methods=["POST"])
def check_credit():
    data = request.get_json()
    income = data.get("income")
    credit_score = data.get("credit_score")
    employment_status = data.get("employment_status")

    # Simple mock scoring logic
    offers = []
    if credit_score >= 700:
        offers.append({"bank": "Bank A", "amount": 50000, "interest_rate": 6.5})
    if income >= 4000:
        offers.append({"bank": "Bank B", "amount": 30000, "interest_rate": 7.2})
    if employment_status == "self-employed":
        offers.append({"bank": "Bank C", "amount": 15000, "interest_rate": 9.9})

    return jsonify({"offers": offers})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    

