from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    user={'username':'lgw'}
    posts = [
        {
            'author':{'username':'lgw'},
            'body':'beautiful day in portland!'
        },
        {
            'author': {'username': 'cjx'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', user=user, posts = posts)