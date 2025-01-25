from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/AboutUs")
def about():
    return "<p>My Name is Sujal</p>"

@app.route("/Login")
def login():
    return "<p>Login Page</p>"


if __name__ == "__main__":
    app.run(port=8000, debug=True)