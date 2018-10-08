from flask import Flask, render_template, session, jsonify, request
import random

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def signup():
    return render_template('signup.html')


@app.route('/forgot')
def forgot_password():
    return "tu password bhul gya great man"


@app.route('/authorize', methods=['POST'])
def authorize():
    data = request.get_json()
    tname = data['t_name']
    print(data, "".join(tname.split()))
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passwd = "".join(random.sample(s, 6))
    return jsonify({"data": data, "username": "".join(tname.split()).lower(), "password": passwd})


if __name__ == '__main__':
    app.run()
