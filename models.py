from os import name
from app import db,app

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True,)
    comment = db.Column(db.String(64), index=True,)

    def __repr__(self):
        return '<User %r>' % (self.comment)