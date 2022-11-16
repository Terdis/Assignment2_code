from flask import Flask, request, render_template, jsonify
from datetime import datetime
from utils import integral

app=Flask(__name__)

@app.route('/')
def hello():
   return render_template("index.html")


@app.route('/<min_x>/<max_x>')
def echo(min_x, max_x):
    values=integral.sinIntegral(float(min_x), float(max_x))
    return jsonify(values)

if __name__=='__main__':
    app.run(debug=True)