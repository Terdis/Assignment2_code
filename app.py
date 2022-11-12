from flask import Flask, request, render_template
from datetime import datetime

app=Flask(__name__)

@app.route('/')
def hello():
   return render_template("index.html")


@app.route('/echo/<name>')
def echo(name):
    return f"Hello {name}"

if __name__=='__main__':
    app.run()