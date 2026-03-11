from book import Book


class BookCollections:

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.remove(book)

    def display_all_books(self):
        for book in self.books:
            print(book.get_info())
