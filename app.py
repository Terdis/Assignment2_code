from flask import Flask, request, render_template, jsonify
from datetime import datetime
from utils import integral

app=Flask(__name__)

@app.route('/')
def hello():
   return render_template("index.html")


@app.route('/<min_x>/<max_x>')
def echo(min_x, max_x):
    initial=datetime.now()
    values=integral.sinIntegral(float(min_x), float(max_x))
    final=datetime.now()
    values[9]=str(final-initial)
    return jsonify(values)

if __name__=='__main__':
    app.run(debug=True)