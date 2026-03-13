from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer)


engine = create_engine('sqlite:///osoba.db', echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_user = User(name="Ala", age=25)
session.add(new_user)
session.commit()

useers = session.query(User).all()
for user in useers:
    print(user.id, user.name, user.age)
# 1 Ala 25
# 2 Ala 25
