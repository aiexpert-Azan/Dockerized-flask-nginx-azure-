from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

# Load baseline data once
with open(os.path.join("data", "baseline.json")) as f:
    baseline_data = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/feature/<feature>")
def feature_info(feature):
    feature_data = baseline_data.get("features", {}).get(feature)
    if not feature_data:
        return jsonify({"error": "Feature not found"}), 404
    return jsonify(feature_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)



