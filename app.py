from flask import *

app = Flask(__name__)
app.debug = True
app.secret_key = "Programmer-RD-AI"


@app.route("/")
def home():
    return render_template("./home/home.html")


if __name__ == "__main__":
    app.run()
