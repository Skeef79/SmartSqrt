from flask import Flask
from flask import render_template, request
from apps import sqrt_logic
import json


app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def index():
    if request.method=="POST":
        data = json.loads(request.data.decode('utf-8'))

        result = sqrt_logic.getSqrt(expr = data["value"], prec = int(data["prec"]))
        resJSON = {
            'res1': result,
            'res2': result
        }

        return json.dumps(resJSON)
        
        return sqrt_logic.getSqrt(expr = data["value"], prec = int(data["prec"]))


    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)