# -*- encoding:utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index/<name>')
def index(name):
    return "hello,world:%s" % name

@app.route('/hello/')
def hello():
    return render_template("demo_hello.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug='True')

