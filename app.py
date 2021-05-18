from flask import Flask
from flask import render_template, request
from apps import sqrt_logic



app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method=="POST":
        expr = request.data.decode('utf-8')
        return sqrt_logic.getSqrt(expr=expr)

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)