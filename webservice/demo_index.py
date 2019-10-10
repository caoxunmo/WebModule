# -*- encoding:utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/index',methods=['GET','POST'])
def modify_IP():
    req_method = request.method
    if req_method == ["GET"]:
        return render_template('index.html')
    else:
        return render_template('demo_hello.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9565', debug=True)
