from flask import Flask, request
from datetime import datetime

app=Flask(__name__)
HELLO_HTML="""
    <html><body>
    <h1> Hello, {0}!</h1>
    </body></html>
"""
@app.route('/')
def hello():
    return "hello Jova!"

@app.route('/echo/<name>')
def echo(name):
    name=request.args['min']
    return HELLO_HTML.format(name, str(datetime.now()))

if __name__=='__main__':
    app.run()