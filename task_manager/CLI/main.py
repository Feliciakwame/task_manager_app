import sys
import os

task_manager_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(task_manager_dir)

from model import database
from model import category
from model import user
from model import task

from task_manager.model.database import engine,Session,Base
from model.task import Task
from model.user import User
from model.category import Category

def create_tables():
    Base.metadata.create_all(engine)
    
def add_task(session,name,user_id,category_id):
    task = Task(name=name,user_id=user_id,category_id=category_id)
    session.add(task)
    session.commit()
    print(f"Task '{name}' added successfully.")
    
def list_tasks(session):
    tasks=session.query(Task).all()
    for task in tasks:
        print(f"[{task.id}] {task.name} -{task.status}")

def mark_task_completed(session,task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.name}' marked as completed.")
    else:
        print(f"Task not found.")
        
def delete_task(session,task_id):
    task = session.query(Task).filter_by(id=task_id).first()
    if task:
        session.delete(task)
        session.commit()
        print(f"Task '{task.name}' deleted.")
    else:
        print(f"Task not found.")
def main():
    create_tables()
    session = Session()

    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter task name: ")
            user_id = int(input("Enter user ID: "))
            category_id = int(input("Enter category ID: "))
            add_task(session, name, user_id, category_id)
        elif choice == "2":
            list_tasks(session)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            mark_task_completed(session, task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(session, task_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice.Try again.")


if __name__ == "__main__":
    main()