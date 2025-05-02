import sqlite3 # Данная СУБД была выбрана благодаря простоте в своем освоении и достаточно легком построении взаимодействия
import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String
from ninja import Ninja
from karate import Karateboy


sqlite3.connect('fighters.db') # Создание базы данных

engine = sqlalchemy.create_engine('sqlite:///fighters.db', echo=True) # Взаимодействие с БД

Base = declarative_base() 


class FighterTable(Base): # Создание турнирной таблицы участников
    __tablename__ = 'fighters'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    health = Column(Integer)
    specific = Column(String(50))

def addinf():
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine) # Начало сессии
    session = Session()

    while input() != 'done': # Добавление новых бойцов в таблицу
        fighter1 = Ninja()
        user = FighterTable(name=fighter1.getName(), health=100, specific=fighter1.getSpec())
        session.add(user)
        fighter2 = Karateboy()
        user = FighterTable(name=fighter2.getName(), health=100, specific=fighter2.getSpec())
        session.add(user)
        session.commit()

    #all_users = session.query(FighterTable).all()
    filtered_users = session.query(FighterTable).filter(FighterTable.specific == 'Ninja').all()
    for users in filtered_users: # Извлечение данных из таблицы
        print(users.name)

    session.close() # Окончание сессии
