from sqlalchemy import ForeignKey, Table, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

Base = declarative_base()

# hotel_customer = Table(
#     'hotel_customers',
#     Base.metadata,
#     Column('hotel_id', ForeignKey('hotels.id'), primary_key=True),
#     Column('customer_id', ForeignKey('customers.id'), primary_key=True),
#     extend_existing=True,
# )

# class Hotel(Base):
#     __tablename__ = 'hotels'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())

#     customers = relationship('Customer', secondary=hotel_customer, back_populates='hotels')
#     # Later: Add 'secondary=hotel_customer' to the relationship

#     reviews = relationship('Review', backref=backref('hotel'), cascade='all, delete-orphan')

#     def __repr__(self):
#         return f'Hotel #{self.id}: {self.name}'
    
# class Customer(Base):
#     __tablename__ = 'customers'

#     id = Column(Integer(), primary_key=True)
#     first_name = Column(String())
#     last_name = Column(String())

#     hotels = relationship('Hotel', secondary=hotel_customer, back_populates='customers')
#     # Later: Add 'secondary=hotel_customer' to the relationship

#     reviews = relationship('Review', backref=backref('customer'), cascade='all, delete-orphan')

#     def __repr__(self):
#         return f'Customer #{self.id}: {self.first_name} {self.last_name}'

# class Review(Base):
#     __tablename__ = 'reviews'

#     id = Column(Integer(), primary_key=True)
#     rating = Column(Integer())

#     hotel_id = Column(Integer(), ForeignKey('hotels.id'))
#     customer_id = Column(Integer(), ForeignKey('customers.id'))

#     def __repr__(self):
#         return f'Review #{self.id}: Rating is {self.rating}'
