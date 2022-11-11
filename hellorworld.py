from flask import Flask
from utils import integral

app=Flask(__name__)

@app.route('/')
def hello():
    sin=integral.sinIntegral(0, 3.14)
    print("###### COMPUTING THE SIN FROM 0 to 3.14")
    print(sin)
    return sin

@app.route('/echo/<name>')
def echo(name):
    return f'Hello {name}'

if __name__=='__main__':
    app.run()