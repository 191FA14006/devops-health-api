from flask import Flask, jsonify
from datetime import datetime
import platform

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Health API Running 🚀"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "system": platform.system(),
        "time": datetime.utcnow().isoformat()
    })

@app.route("/time")
def time():
    return jsonify({
        "current_time": datetime.utcnow().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
