from sqlalchemy import Column
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import String

class State(BaseModel, Base):
    """This class represents a state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan', backref='state')
