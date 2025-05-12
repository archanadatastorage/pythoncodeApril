from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found!"}), 404

@app.route("/")
def home():
	 return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(debug=True)