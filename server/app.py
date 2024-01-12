#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()
    if not animal:
        response_body = '<h1>404 animal not found </h1>'
        response = make_response(response_body, 404)
        return response
    
    # zookeeper = Zookeeper.query.filter(Zookeeper.id == animal.zookeeper).first()
    # enclosure = Enclosure.query.filter(Enclosure.id == animal.enclosure).first()
    
    # <ul>ID: {animal.id}</ul>
    # <ul> Zookeeper: {animal.zookeeper.name}</ul>
                # <ul> Enclosure: {animal.enclosure.environment}</ul>
    
    return f''' 
                <ul> Name: {animal.name}</ul>
                <ul> Species: {animal.species}</ul>                

'''

@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()
    
    if not zookeeper:
        response_body = '<h1>404 Zookeeper not found </h1>'
        response = make_response(response_body, 404)
        return response
    
    animals_list = ''.join([f'<h1>Animal: {animal.name}</h1>' for animal in zookeeper.animals])
    
    return f''' <h1>ID: {zookeeper.id} </h1>
                <h1> Name: {zookeeper.name}</h1>
                <h1> Birthday: {zookeeper.birthday}</h1>
                <ul>{animals_list}</ul>
                

'''

@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()
    
    animals_list = ''.join([f'<h1>Animal: {animal.name}</h1>' for animal in enclosure.animals])
    
    
    return f''' <h1>ID: {enclosure.id} </h1>
                <h1> Emvironment: {enclosure.environment}</h1>
                <h1> Open to Visitors: {enclosure.open_to_visitors}</h1>
                <ul>{animals_list}</ul>
                

'''


if __name__ == '__main__':
    app.run(port=5555, debug=True)
