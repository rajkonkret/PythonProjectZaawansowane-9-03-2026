from day3.filmy.film import Film


class DocumantaryFilm(Film):
    def play(self):
        print(f"Odtwarzaanie filmu dokumentalnego: {self.title}")

    def get_info(self):
        return f"{self.title}, reżyseria: {self.director}, produkcja: {self.year}, czas trwania [h]: {self.duration}"