#!/usr/bin/python3
"""
This script creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""
from sys import argv
from sqlalchemy import create_engine
from relationship_state import State
from relationship_city import City, Base
from sqlalchemy.orm import sessionmaker, relationship

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_city = City(name="San Francisco")
    new_city.state = State(name="California")
    session.add(new_city)
    # session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
    session.close()