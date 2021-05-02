from flask import Flask, redirect, url_for ,render_template,request
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.absname(__file__))
database_file = 'sqlite:///{}'.format(os.path.join(project_dir, 'mydatabase.db'))

app = Flask(__name__)
app.config['SQLACHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username, isActive=False)

@app.route('/books')
def books():
    books=[
            {'name':'book1','author':'Tanisha', 'cover':'https://images.template.net/wp-content/uploads/2014/05/Vintage-Book-Cover-Template.jpg'},
            {'name':'book2','author':'Anisha', 'cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-7-CRC.png'},
            {'name':'book3','author':'Nisha', 'cover':'https://i.pinimg.com/474x/f7/c8/12/f7c812c9b0296cd9f119e33a06d9a256.jpg'},
            {'name':'book4','author':'Isha', 'cover':'https://d1csarkz8obe9u.cloudfront.net/posterpreviews/contemporary-fiction-night-time-book-cover-design-template-1be47835c3058eb42211574e0c4ed8bf_screen.jpg?ts=1594616847'}
          ]
    return render_template('book.html', books=books)

@app.route('/addbook')
def addbook():
    return render_template('addbook.html')

@app.route('/submitform', methods = ['POST'])
def submitform():
    name = request.form['name']
    author= request.form['author']
    return 'Book name is %s and authour is %s' %(name , author)
app.run(debug= True)