import logging
from peewee import *

logger = logging.getLogger("peewee")
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

db = SqliteDatabase("test.db")

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    name = CharField()
    age = IntegerField()

db.connect()
db.create_tables([User])

User.create(name="Jan", age=30)
User.create(name="Anna", age=25)

users = User.select().where(User.age > 20)
for u in users:
    print(u.name, u.age)