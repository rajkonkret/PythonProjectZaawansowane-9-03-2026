from film_collection import FilmCollection
from kinds.action import ActionFilm
from kinds.comedy import ComedyFilm
from kinds.document import DocumantaryFilm

collections = FilmCollection()
film1 = ActionFilm("Mad Max: Fury Road", "George Orwell", 2015, 2)
film2 = ComedyFilm("The Grand Budapest Hotel", "Wes Anderson", 2014, 1.75,
                   "Wes anderson's Universe", 1)

film3 = DocumantaryFilm("The Social Dilema", "Jeff Orlowsky", 202, 1.7)

film1.add_award("Oscar za najlepszy montaż")
film1.add_award("Oscar za najlepszy dźwiek")

collections.add_film(film1)
collections.add_film(film2)
collections.add_film(film3)

collections.dispaly_all_films()

film1.play()
film2.play()
# Utworzono nowy obiekt oparty na klasie ActionFilm
# Utworzono nowy obiekt oparty na klasie ComedyFilm
# Utworzono nowy obiekt oparty na klasie DocumantaryFilm
# Mad Max: Fury Road, reżyseria: George Orwell, produkcja: 2015, czas trwania [h]: 2 | Nagrody: Oscar za najlepszy montaż,Oscar za najlepszy dźwiek
# The Grand Budapest Hotel, rezyseria: Wes Anderson, produkcja: 2014, czas trwania [h]: Wes Anderson | Seria: Wes anderson's Universe, cześć: 1
# The Social Dilema, reżyseria: Jeff Orlowsky, produkcja: 202, czas trwania [h]: 1.7
# Odtwarzanie filmu akcji: Mad Max: Fury Road
# Odtwarzanie komedii: The Grand Budapest Hotel
