from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
from app import db
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __init__(self,id,name):
        self.name = name
        self.id =id

    # Gets dict with the Doctor object and all of its associated reviews
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name
        }
