from flask import Flask, redirect, url_for 
app = Flask(__name__)
@app.route('/index/<username>')
def index(username):
    return 'Welcome %s'%username

@app.route('/admin')
def admin():
    return 'welcome admin'

@app.route('/profile/<name>')
def profile(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('index', username=name))
app.run(debug= True)