class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(book)

# Usage:
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Science Essentials", "Alice Johnson")

bookstore = Bookstore()
bookstore.add_book(book1)
bookstore.add_book(book2)

print("Books in the Bookstore:")
bookstore.display_books()
