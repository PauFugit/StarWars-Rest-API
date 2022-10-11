from weakref import ReferenceType
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    fav_characters = db.Integer,db.ForeignKey('FavCharacter_id')
    fav_starships = db.Integer, db.ForeignKey('FavStarship_id')
    fav_planets = db.Integer, db.ForeignKey('FavPlanet_id')
    
    def serialize(self):
        return {
            "id": self.id,
            "username" : self.username,
            "email": self.email,

        }

    def favorites(self):
        array =[]
        characters = list(map(lambda characters: characters.serialize(), self.fav_characters))
        starships = list(map(lambda starships: starships.serialize(), self.fav_starships))
        planets = list(map(lambda planets: planets.serialize(), self.fav_planets))
        for character in characters: array.append(character)
        for starship in starships: array.append(starship)
        for planet in planets: array.append(planet)
        return array

    def serialize_favorites(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "favorites": self.favorites()
        }


    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




class FavCharacter(db.Model):
    __tablename__= 'favorite_characters'
    id = db.Column(db.Integer, primary_key=True)
    character = db.Integer, db.ForeignKey('Characters_id')
    user = db.Integer, db.ForeignKey('User_id')

    def serialize(self):
        return{
            "id": self.id,
            "character": self.character,
            "user": self.user,
        }

    def dave(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.sesssion.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class FavStarship(db.Model):
    __tablename__= 'favorite_starships'
    id = db.Column(db.Integer, primary_key=True)
    starship = db.Integer, db.ForeignKey('Starships_id')
    user = db.Integer, db.ForeignKey('User_id')

    def serialize(self):
        return{
            "id": self.id,
            "starship": self.starship,
            "user": self.user,
        }

    def dave(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.sesssion.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class FavPlanet(db.Model):
    __tablename__= 'favorite_planets'
    id = db.Column(db.Integer, primary_key=True)
    planet = db.Integer, db.ForeignKey('Planets_id')
    user = db.Integer, db.ForeignKey('User_id')

    def serialize(self):
        return{
            "id": self.id,
            "planet": self.planet,
            "user": self.user,
        }

    def dave(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.sesssion.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Characters(db.Model):
    __tablename__= 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    height = db.Column(db.String(100))
    mass = db.Column(db.String(100))
    eye_color = db.Column(db.String(20))
    birth_year = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    image = db.Column(db.String(100))

    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "image": self.image,
        }

    def dave(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.sesssion.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    model = db.Column(db.String(100), unique=True)
    manufacturer = db.Column(db.String(100))
    cost_in_credits = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers = db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)
    length = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(250))


    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "manufacturer": self.manufacturer,
            "cost_in_credits": self.cost_in_credits,
            "crew": self.crew,
            "passengers": self.passengers,
            "cargo_capacity": self.cargo_capacity,
            "length": self.length,
            "image": self.image,
        }

    def dave(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.sesssion.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(100))
    surface_water = db.Column(db.String(50))
    population = db.Column(db.Integer)
    gravity = db.Column(db.String(100))
    image = db.Column(db.String(100))


    def serialize(self):
        return{
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "surface_water": self.surface_water,
            "population": self.population,
            "gravity": self.gravity,
            "image": self.image,
        }

    def dave(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.sesssion.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

