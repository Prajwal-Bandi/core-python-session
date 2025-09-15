from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float, Boolean

# Initialize SQLAlchemy
db = SQLAlchemy()

# Define the Employee model
class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)
    salary = Column(Float, nullable=False)
    is_active = Column(Boolean, nullable=False)

    def __repr__(self):
        return (f'id={self.id}, name={self.name}, age={self.age}, '
                f'salary={self.salary}, is_active={self.is_active}')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'salary': self.salary,
            'is_active': self.is_active
        }
