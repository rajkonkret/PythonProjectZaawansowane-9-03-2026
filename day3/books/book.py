from abc import ABC, abstractmethod


class Book(ABC):
    """
    Klasa Book
    """

    def __init__(self, title, author, year, pages):
        """
        Metoda inicjalizująca
        """
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __repr__(self):
        return f"Obiekt klasy {self.__class__.__name__} ({self.title} -> {self.author}"

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def read(self):
        pass
