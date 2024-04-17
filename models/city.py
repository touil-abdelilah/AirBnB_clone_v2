from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import String

class City(BaseModel, Base):
    """This class represents a city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
