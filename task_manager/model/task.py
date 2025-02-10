from sqlalchemy import Column,Integer ,String , Foreignkey
from sqlalchemy.orm import relationship
from task_manager.model.database import Base

class Task(Base):
    __tablename__ ='tasks'
    
    id= Column(Integer,primary_key=True)
    name=Column(String,nullable=False)
    status=Column(String,default="Pending")
    user_id = Column(Integer,ForeignKey("users.id"))
    category_id = Column(Integer,ForeignKey("categories.id"))
    
    user=relationship("User", back_populates="tasks")
    category = relationship("Category",back_populates="tasks")
    
    def __repr__(self):
        return f"<Task(id={self.id},name={self.name},status={self.status})>"