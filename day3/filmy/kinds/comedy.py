from idlelib.debugobj import ClassTreeItem

from day3.filmy.film import Film
from day3.filmy.series import SeriesPart


class ComedyFilm(Film, SeriesPart):
    def __init__(self, title: str, director: str, year: int, duration: float, series_name: str, part_number: int):
        Film.__init__(self, title, director, year, duration)
        SeriesPart.__init__(self, series_name, part_number)

    def play(self):
        print(f"Odtwarzanie komedii: {self.title}")

    def get_info(self):
        info = f"{self.title}, rezyseria: {self.director}, produkcja: {self.year}, czas trwania [h]: {self.director}"
        series_info = self.get_series_info()
        info += f' | {series_info}'
        return info

if __name__ == '__main__':
    print(ComedyFilm.__mro__)
# (<class '__main__.ComedyFilm'>, <class 'day3.filmy.film.Film'>, <class 'abc.ABC'>, <class 'day3.filmy.series.SeriesPart'>, <class 'object'>)
