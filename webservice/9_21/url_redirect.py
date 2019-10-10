# -*- encoding:utf-8 -*-

from flask import Flask,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/login/')
def login_in():
    return "login in"

@app.route('/test/<id>')
def test_id(id):
    return "test the %s" % id

@app.route('/show/')
def show():
    #1、返回视图函数所对应的URL
    print(url_for("index"))
    print(url_for("login_in"))

    #2、带参数的URL，把对应参数的值以关键字参数的形式传入
    print(url_for("test_id", id=123))

    #3、当给出的关键字参数不是对应URL的参数时，将其作为查询参数添加到URL中
    print(url_for("login_in", usrname="momo", passwd="0000"))

    #4、url_for可以正确的处理空格等字符的URL编码问题
    print(url_for("test_id", id="123", first="111", second="222"))

    return "redirect"






if __name__ == '__main__':
    app.run(host='0.0.0.0', port='7556', debug=True)