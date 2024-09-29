from app import db
from dataclasses import dataclass

@dataclass
class Task(db.Model):
    id:int = db.Column(db.Integer, primary_key=True)
    name:str = db.Column(db.String(255), nullable=False)
    content:str = db.Column(db.Text)

    def __repr__(self):
        return f'<Task {self.firstname}>'