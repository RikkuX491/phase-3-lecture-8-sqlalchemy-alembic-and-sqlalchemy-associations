from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Hotel

if __name__ == '__main__':
    pass
    
    # engine = create_engine('sqlite:///hotels.db')
    # Session = sessionmaker(bind=engine)
    # session = Session()

    # hotel1 = Hotel(name="Marriott")
    # hotel2 = Hotel(name="Hampton Inn")
    # hotel3 = Hotel(name="Holiday Inn")

    # session.add_all([hotel1, hotel2, hotel3])
    # session.commit()
