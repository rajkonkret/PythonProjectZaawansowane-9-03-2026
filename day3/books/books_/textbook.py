from day3.books.book import Book


class TextBook(Book):
    def get_info(self):
        return f"{self.title} ({self.author}, {self.year}, {self.pages})"

    def read(self):
        print(f"Przeczytana podręcznik {self.title}. Zawiera dodatkowe materiały")
