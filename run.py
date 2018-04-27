from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config.update(

    SECRET_KEY='ncrd99',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:ncrd99@localhost/catalog_db',
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    )

db = SQLAlchemy(app)


@app.route('/watch')
@app.route('/')
def movies_2018():
    movie_list = ['movie1', 'movie2', 'movie3']

    return render_template('movies.html',
                           movies=movie_list,
                           name='Esraa')


class Publication(db.Model):
    __tablename__ = "publication"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, name):
        # called when new instance are created
        self.name = name

    def __repr__(self):
        # string representation of an instance
        return 'Name is {}'.format(self.name)


class Book(db.Model):
    __tabelname__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False, index=True)
    author = db.Column(db.String(350))
    avg_rating = db.Column(db.Float)
    format = db.Column(db.String(50))
    image = db.Column(db.String(100), unique=True)
    num_pages = db.Column(db.Integer)
    pub_date = db.Column(db.DateTime, default=datetime.utcnow())
     # Relationship
    pub_id = db.Column(db.Integer, db.ForeignKey('publication.id'))

    def __init__(self, title, author, avg_rating, book_format, image, num_pages, pub_id):
        self.author = author
        self.title = title
        self.avg_rating = avg_rating
        self.format = book_format
        self.image = image
        self.num_pages = num_pages
        self.pub_id = pub_id

    def __repr__(self):
        return '{} by {}'.format(self.title, self.author)


if __name__ == '__main__':
    db.create_all()  # create all the tables if they are not exists
    app.run(debug=True)











