from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_ghw():
    return "<p>Hello, World , Kunal Here!</p>"


if __name__ == "__main__":
    app.run(debug=True)