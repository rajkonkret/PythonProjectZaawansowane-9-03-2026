from day3.books.book import Book

class Novel(Book):
    def get_info(self):
        return f"{self.title} ({self.author}, {self.year}, {self.pages} stron)."

    def read(self):
        print(f"Przeczytano powieść {self.title}")
