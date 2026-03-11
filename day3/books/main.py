from book_collection import BookCollections
from books_.novel import Novel
from books_.textbook import TextBook

collection = BookCollections()
novel = Novel("1984", "George Orwell", 1949, 328)
textbook = TextBook("Python programming", "John Brown", 2021, 467)

collection.add_book(novel)
collection.add_book(textbook)

collection.display_all_books()

novel.read()
textbook.read()

print("pokaż obiekty")
print(novel)
print(textbook)
