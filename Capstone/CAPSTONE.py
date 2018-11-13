class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.book = {}

    def get_email(self):
        if self.name == name:
            return self.email

    def change_email(self, address):
        self.email = email
        self.address = self.email.replace(email, address)
        return "This User's email has been updated."

    def __repr__(self):
        return "User {name}, email: {email}, books read: {}".format(name=name, email=email, books=books)

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_books(book, rating = None):
        self.book.get(str(book))

    def get_average_rating():
        total_rating = 0
        for rting in self.book:
            total_rating += rting
        get_average = total_rating / int(len(self.book))
        return get_average


class Book:
    def __init__(self, title, isbn):
          self.title = str(title)
          self.isbn = int(self.isbn)
          self.rating = []

    def get_title():
        return title

    def get_isbn():
        return isbn

    def set_isbn(self, new_isbn):
        self.isbn = isbn
        self.new_isbn = self.isbn.replace(isbn, new_isbn)
        return "This book's ISBN has been updated."

    def add_rating():
        rating = 0
        if rating >= 0 and rating <=4:
            self.rating += rating
        else:
            return "Invalid Rating"

    def __eq__(self, other_book):
        return self.title == other_book.tittle and self.isbn == other_book.isbn

    def get_average_rating():
        rating = 0
        rating += self.rating.pop(book, 0)
        return rating / 2

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_author():
        return author

    def __repr__(self):
        return "{title} by {author}".format(title=title, author=author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        self.title = title
        self.subject = subject
        self.level = level
        self.isbn = isbn

    def get_subject():
        return subject

    def get_level():
        return level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=title, level=level, subject=subject)

class TomeRater:
    pass