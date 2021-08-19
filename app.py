from flask import Flask, request , render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
db.create_all()


from models import Comment

@app.route('/', methods=['POST', 'GET'])
def index(name=''):
    try:
        comments = Comment.query.all()
    except:
        comments = None    
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        c = Comment(name=name, comment=comment)
        db.session.add(c)
        db.session.commit()    
        return redirect(url_for('index'))   
    return render_template('index.html', comments=comments)    
