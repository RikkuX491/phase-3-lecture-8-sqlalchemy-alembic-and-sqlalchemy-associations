from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class Hotel(Base):
#     __tablename__ = 'hotels'

#     id = Column(Integer(), primary_key=True)
#     name = Column(String())

#     def __repr__(self):
#         return f'Hotel #{self.id}: {self.name}'
