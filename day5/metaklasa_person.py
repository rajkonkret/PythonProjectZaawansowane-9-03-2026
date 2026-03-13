from dataclasses import dataclass, Field
from datetime import datetime

# Field: default, default_factory, init, repr, hash, compare, kw_only

params = {
    "firstname": Field(None, None, True, True, True, True, None, None, None),
    "lastname": Field(None, None, True, True, True, True, None, None, None),
    "year_of_birth": Field(None, None, True, True, True, True, None, None, None),
}


def age(self):
    return datetime.now().year - self.year_of_birth


MetaPerson = dataclass(type("MetaPerson", (), {'__annotations__': params, "wiekosoby": property(age)}))

p = MetaPerson("Roman", "Tracz", 1976)
print(p)  # MetaPerson(firstname='Roman', lastname='Tracz', year_of_birth=1976)
print(type(p))  # <class '__main__.MetaPerson'>
print(p.wiekosoby)  # 50
