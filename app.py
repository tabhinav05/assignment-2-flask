from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Professor Ziyad, Assignment 2 by Abhinav Tanwar - 100940786 ."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


