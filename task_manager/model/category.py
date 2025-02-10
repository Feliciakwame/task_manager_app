from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from task_manager.model.database import Base

class Category(Base):
    __tablename__="categories"
    
    id = Column(Integer,primary_key=True)
    name = Column(String,nullable=False,unique=True)
    tasks = relationship("Task",back_populates="category")
    
    def __repr__(self):
        return f"<Category(id={self.id},name={self.name})>"