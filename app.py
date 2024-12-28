from flask import Flask, render_template, jsonify
from selenium_scraper import main

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run-script', methods=["GET"])
def run_script():
    result = main()
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
