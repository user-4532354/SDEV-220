#Nailah Pierre
#4/14/24
#M04 Lab - Case Study: Python APIs




from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()


class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  author = db.Column(db.String(120), nullable=False)
  publisher = db.Column(db.String(400), nullable=False)

  def __repr__(self):
    return f"{self.name} - {self.author} - {self.publisher}"



@app.route('/')
def index():
  return "Hello World"

@app.route('/books')
def get_books():
    book = Book.query.all()

    output = []
    for book in books:
        book_data = {"name": book.name, "author": book.author, "publisher": book.publisher}
        output.append(book_data)

    return {'books': output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return ["name": book.name, "author": book.author, "publisher": book.publisher]



@app.route('/books', methods=[POST])
def add_drink():
    book = Book(name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}



@app.route('/books/<id>', methods=['DELETE'])
def delete_book():
    book = Book.query.get(id)
    if book is None:
        return {"error": : "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "yeet!"}









