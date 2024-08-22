from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey


db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, nullable=False )
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    favorite_planet = db.relationship('Favorite_planet')
    favorite_character = db.relationship('Favorite_character')

    def serialize(self):
        return {
            "id": self.id,
            "age": self.age,
            "name": self.name,
            "email": self.email,
            "favorite_planet": self.favorite_planet,
            "favorite_character": self.favorite_character,
        }
    
    def __repr__(self):
        return '<User %r>' % self.username
    
class Favorite_planet(db.Model):
    __tablename__ = 'favorite_planet'
    user_primary_id = db.Column(db.Integer, primary_key=True)
    planet_primary_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id') )
    planet_id = db.Column(db.Integer, ForeignKey('planet.id') )

    def serialize(self):
        return {
            "user_primary_id": self.user_primary_id,
            "planet_primary_id": self.planet_primary_id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
        }
    def __repr__(self):
        return '<Favorite_planet %r>' % self.planet_primary_id
    
class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(100), unique= True, nullable=False)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    gravity = db.Column(db.String(50))
    terrain = db.Column(db.String(50)) 
    surface_water = db.Column(db.Integer)
    population = db.Column(db.Integer)
    planet = db.relationship('Favorite_planet') 

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population": self.population,
            "planet": self.planet,
        }
    def __repr__(self):
        return '<Planet %r>' % self.name
    
class Favorite_character(db.Model):
    __tablename__ = 'favorite_character'
    user_primary_id = db.Column(db.Integer, primary_key=True)
    character_primary_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id') )
    character_id = db.Column(db.Integer, ForeignKey('character.id') )

    def serialize(self):
        return {
            "user_primary_id": self.user_primary_id,
            "character_primary_id": self.character_primary_id,
            "user_id": self.user_id,
            "character_id": self.character_id,
        }
    
    def __repr__(self):
        return '<Favorite_character %r >' % self.character_primary_id
    
class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key= True)
    description = db.Column(db.String(200))
    name = db.Column(db.String(200 ), unique= True, nullable=False )
    skin_color = db.Column(db.String(20))
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(20))
    gender = db.Column(db.String(20)) 
    eye_color = db.Column(db.String(200))
    planet_id = db.Column(db.Integer)
    film_id = db.Column(db.Integer)
    favorite_character = db.relationship('Favorite_character')

    def serialize(self):
        return {
            "id": self.id,
            "description": self.description,
            "name": self.name,
            "skin_color": self.skin_color,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "gender": self.gender,
            "eye_color": self.eye_color,
            "planet_id": self.planet_id,
            "film_id": self.film_id,
            "favorite_character": self.favorite_character,
        }
    
    def __repr__(self):
        return '<Character %r>' % self.name
    