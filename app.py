from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello giov"

@app.route('/echo/<name>')
def echo(name):
    return f'Hello {name}'

if __name__=='__main__':
    app.run()