from app import app
from flask import render_template
from datetime import date, datetime

@app.route('/')
def index(): 
    context ={
        'first_name': 'Steve',
        'last_name' : 'Rodgers',
        'email' : 'SteveRodgers@marvel.com',
        'posts' : [
            {
                'id': 1,
                'body': 'Cap and his favorite heroes',
                'date_created': datetime.utcnow()
            },
            {
                'id': 2,
                'body': 'Cap knows all your favorite heroes',
                'date_created': datetime.utcnow()
            },
            {
                'id': 3,
                'body': 'Cap tells you his favorite foes',
                'date_created': datetime.utcnow()
            },
        ]
    }   
    return render_template('index.html', **context)

@app.route('/about')
def about():
    data = {
        'first_name': 'Steve',
        'last_name': 'Rodgers'
    }
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/register')
def register():
    return render_template('register.html')