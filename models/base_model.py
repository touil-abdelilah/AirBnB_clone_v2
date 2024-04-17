from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime

Base = declarative_base()

class BaseModel:
    """This class defines common attributes/methods for other classes"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize instance attributes"""
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                if k != '__class__':
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Save current instance to the storage"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        result = dict(self.__dict__)
        result['__class__'] = self.__class__.__name__
        result['created_at'] = self.created_at.isoformat()
        result['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in result:
            del result['_sa_instance_state']
        return result

    def delete(self):
        """Delete the current instance from storage"""
        from models import storage
        storage.delete(self)

