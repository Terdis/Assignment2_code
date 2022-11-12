from flask import Flask, request, render_template, jsonify
from datetime import datetime
from utils import integral

app=Flask(__name__)

@app.route('/')
def hello():
   return render_template("index.html")


@app.route('/<min_max>')
def echo(min_max):
    min, max=min_max.split("_")

    values={'values' : integral.sinIntegral(float(min), float(max)).tolist()}
    return jsonify(values)

if __name__=='__main__':
    app.run(debug=True)