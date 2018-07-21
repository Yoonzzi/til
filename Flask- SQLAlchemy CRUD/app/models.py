from app import db

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    content = db.Column(db.Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content