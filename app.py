from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
DATABASE_URL = 'postgresql://postgres:Yuvi%40123@localhost:5433/login_db'
app.config.update(
        SECRET_KEY = "ASDFGHJKL",
        SQLALCHEMY_DATABASE_URI = DATABASE_URL,
        SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(app)
app.app_context().push()

class Publication(db.Model):

    __tablename__ = 'publication'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
     
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Name is {self.name}"

class Book(db.Model):

    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(500), nullable = False, index = True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100),unique =True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default = datetime.utcnow())

    #Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, format, image, num_pages, pub_id):
        self.title = title
        self.author = author
        self.avg_rating = avg_rating
        self.format = format
        self.image =  image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return f"{self.title} is title, {self.author} is author"

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)