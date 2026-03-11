class NotFound(Exception):
    def __init__(self, resource, resource_id):
        msg = f'{resource} o ID {resource_id} nie znaleziono'
        super().__init__(msg)
        self.resource = resource
        self.resource_id = resource_id

    @staticmethod
    def for_any(resource, resource_id):
        return NotFound(resource, resource_id)

    @classmethod
    def user(cls, user_id):
        return cls("Użytkownik", user_id)


# raise NotFound.user(7)
# Traceback (most recent call last):
#   File "C:\Users\cscomarch\PycharmProjects\PythonProjectZaawansowane-9-03-2026\day3\wlasny_wyjatek_classmethod.py", line 17, in <module>
#     raise NotFound.user(7)
# NotFound: Użytkownik o ID 7 nie znaleziono

raise NotFound.for_any('dokument', 45)  # NotFound: dokument o ID 45 nie znaleziono
