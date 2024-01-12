from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from datetime import datetime

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'  
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.DateTime)
    animals = db.relationship('Animal', backref='zookeeper')
    
    def __repr__(self):
        return F'<Zookeper {self.name}, Animals: {self.animals}>'

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)
    animals = db.relationship('Animal', backref='enclosure')
    
    def __repr__(self):
        return f'<Enclosure: env: {self.environment} animals: {self.animals}>'

class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)
    zookeeper_id = db.Column(db.Integer, db.ForeignKey ('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    
    def __repr__(self):
        return f'<Animal Name: {self.name} Species: {self.species} Zookeper_id: {self.zookeeper_id} enclosure: {self.enclosure_id}>'
