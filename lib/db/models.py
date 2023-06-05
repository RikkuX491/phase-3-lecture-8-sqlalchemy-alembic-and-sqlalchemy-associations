from sqlalchemy import ForeignKey, Column, Integer, String, MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

convention = {
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
}

m = MetaData(naming_convention=convention)

Base = declarative_base(metadata=m)

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    reviews = relationship('Review', backref='hotel')
    customers = association_proxy('reviews', 'customer',
        creator=lambda c: Review(customer=c))

    def __repr__(self):
        return f'Hotel #{self.id}: {self.name}'

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(String())

    hotel_id = Column(Integer(), ForeignKey('hotels.id'))
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f'Review #{self.id}: Rating is {self.rating}, left by {self.customer.first_name} {self.customer.last_name} for {self.hotel.name} hotel.'

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())

    reviews = relationship('Review', backref='customer')
    hotels = association_proxy('reviews', 'hotel',
        creator=lambda h: Review(hotel=h))
    
    def __repr__(self):
        return f'Customer #{self.id}: {self.first_name} {self.last_name}'