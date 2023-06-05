import ipdb
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Hotel

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///db/hotels.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ipdb.set_trace()

    # Create
    # hotel = Hotel(name="The Chanler at Cliff Walk")
    # session.add(hotel)
    # session.commit()

    # Read
    # hotels = session.query(Hotel)
    # print(f"There are {hotels.count()} hotels available!")
    # print("Here is the info of all available hotels:")
    # for hotel in hotels:
    #     print(hotel)

    # Update
    # hotel_to_update = session.query(Hotel).filter(Hotel.id == 4).first()
    # hotel_to_update.name = "Flatiron School Resort"
    # session.commit()

    # Delete a specific hotel from the database
    # hotel = session.query(Hotel).filter(Hotel.id == 4).first()
    # session.delete(hotel)
    # session.commit()

    # Delete all hotels from the hotels table
    # hotels = session.query(Hotel).delete()
    # session.commit()
