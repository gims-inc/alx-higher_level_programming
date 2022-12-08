#!/usr/bin/python3
"""
Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa.
Usage: ./<this-file-name> <mysql username> /
                          <mysql password> /
                          <database name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    url = f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}\
                             @localhost/{sys.argv[3]}'
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    S = sessionmaker(bind=engine)
    session = S()

    session.ass(City(name="San Francisco", state=State(name="California")))
    session.commit()
