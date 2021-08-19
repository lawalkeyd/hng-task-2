from flask import Flask, request , render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)

from models import Comment

@app.route('/', methods=['POST', 'GET'])
def index(name=''):
    db.create_all()
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
        return render_template('index.html', comments=comments)    
    return render_template('index.html', comments=comments)    
