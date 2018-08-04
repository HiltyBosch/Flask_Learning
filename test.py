from flask import Flask,abort,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401);
    return 'hahaha'

@app.errorhandler(401)
def errHandler(error):
    return "errorhhahaha"

