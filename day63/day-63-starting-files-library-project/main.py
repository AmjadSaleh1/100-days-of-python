from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def home():
    all_books = []
    result = db.session.execute(db.select(Book).order_by(Book.title))
    for book in result.scalars():
        booke = {
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "rating": book.rating,
        }
        all_books.append(booke)
    return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET', 'POSt'])
def add():
    if request.method == 'POST':
        with app.app_context():
            new_book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/<tid>", methods=["GET", "POST"])
def edit(tid):
    book_to_update = db.session.execute(db.select(Book).where(Book.id == tid)).scalar()
    if request.method == "POST":
        with app.app_context():
            book_to_update = db.session.execute(db.select(Book).where(Book.id == tid)).scalar()
            book_to_update.rating = request.form['rating']
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", tid=tid, book=book_to_update)


@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
