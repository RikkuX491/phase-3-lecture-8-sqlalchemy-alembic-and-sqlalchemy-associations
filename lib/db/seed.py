from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Hotel
from models import Customer
from models import Review

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///hotels.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # hotel1 = Hotel(name="Marriott")
    # hotel2 = Hotel(name="Hampton Inn")
    # hotel3 = Hotel(name="Holiday Inn")

    # customer1 = Customer(first_name="Alice", last_name="Baker")
    # customer2 = Customer(first_name="Brendan", last_name="Johnson")
    # customer3 = Customer(first_name="Chris", last_name="Smith")

    # review1 = Review(rating=5, hotel_id=1, customer_id=1)
    # review2 = Review(rating=5, hotel_id=2, customer_id=1)
    # review3 = Review(rating=4, hotel_id=1, customer_id=2)
    # review4 = Review(rating=3, hotel_id=1, customer_id=1)

    # session.add_all([hotel1, hotel2, hotel3, customer1, customer2, customer3, review1, review2, review3, review4])
    # session.commit()