from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/echo/<name>')
def echo(name):
    return f'Hello {name}'

if __name__=='__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)