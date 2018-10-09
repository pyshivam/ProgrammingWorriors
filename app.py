from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient
import random

app = Flask(__name__)


class DataBase:
    def __init__(self, database="programming"):
        self.client = MongoClient()
        self.db = self.client[database]

    def insert_user(self, data):
        if self.user_check(username=data['username'])["status"]:
            return {"status": 0, "message": "User already exists."}
        else:
            table = self.db['users']
            table.insert(data)
            return {"status": 1, "message": "User added successfully."}

    def user_check(self, username, password=None):
        table = self.db['users']
        account = table.find_one({
            'username': username
        })
        if account:
            username = account['username']
            passwd = account['passwd']
            if password == passwd:
                return {"status": 1, "name": username, "message": "User logged in."}
            elif password != passwd and password is not None:
                return {"status": 0, "message": "Wrong password."}
            return {"status": 1, "username": username, "password": passwd}
        else:
            return {"status": 0, "message": "User not found"}

    def delete_user(self, username):
        table = self.db["users"]
        if self.user_check(username=username)["status"]:
            res = table.delete_one({"username": username})
            print(res)
            return {"status": 1, "message": "User removed successfully."}
        else:
            return {"status": 0, "message": "User not exists."}


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
    db = DataBase()
    data = request.get_json()
    if not data:
        data = {
            "clg_name": request.form['clg_name'],
            "prof_name": request.form['prof_name'],
            "prof_email": request.form['prof_email'],
            "phone": request.form['phone'],
            "t_name": request.form['t_name'],
            "student_name1": request.form['student_name1'],
            "student_name2": request.form['student_name2'],
            "t_number": request.form['t_number'],
            "email": request.form['email'],
            "auth": request.form['auth']
        }
    tname = data['t_name']

    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    passwd = "".join(random.sample(s, 6))
    username = "".join(tname.split()).lower()
    data['passwd'] = passwd
    data['username'] = username
    print(data, "".join(tname.split()))
    db.insert_user(data=data)

    return jsonify({"status": 1, "username": username, "password": passwd})


if __name__ == '__main__':
    app.run()
