from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/process")
def process():
    return jsonify({"message": "Processed by Worker!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
