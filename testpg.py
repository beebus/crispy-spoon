from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgres://bfcvgvezioizyk:3979009eb1b0ea2642a9c83606b515b5ad395454f702523dee9b2a89e3429dd2@ec2-174-129" \
            "-242-183.compute-1.amazonaws.com:5432/d7t7o3ehhinlck"

db = create_engine(db_string)

base = declarative_base()


class Fruit(base):
    __tablename__ = 'fruits'

    name = Column(String, primary_key=True)
    color = Column(String)


Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

firstfruit = Fruit(name='apple', color='red')
session.add(firstfruit)
session.commit()

fruits = session.query(Fruit)
for fruit in fruits:
    print(fruit.name)
session.delete(fruit)
session.commit()

Fruit.__table__.drop(db)
