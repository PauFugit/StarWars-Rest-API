
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from models import db, User, Characters, Starships, Planets, FavCharacter, FavPlanet, FavStarship

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbstarwars'
db.init_app(app)
Migrate(app, db)
CORS(app)


#ppal 

@app.route('/')
def main():
    return jsonify({
        "msg": "Welcome to my Star Wars API"
    }), 200

# all users

@app.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':
        users = User.query.all()
        users = list(map(lambda user: user.serialize(), users))
        return jsonify(users), 200

    if request.method == 'POST':
        
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        fav_characters = request.json.get('fav_characters')
        fav_starships = request.json.get('fav_starships')
        fav_planets = request.json.get('fav_planets')

        user = User()
        user.username = username
        user.email = email
        user.password = password
        
        if fav_characters:
            for FavCharacter_id in fav_characters:
                people = FavCharacter.query.get(FavCharacter_id)
                user.fav_characters.append(people)

        if fav_starships:
            for FavStarship_id in fav_starships:
                vehicle = FavStarship.query.get(FavStarship_id)
                user.fav_starships.append(vehicle)

        if fav_planets:
            for FavPlanet_id in fav_planets:
                location = FavPlanet.query.get(FavPlanet_id)
                user.fav_planets.append(location)

        user.save()

        return jsonify(user.serialize()), 201
        

#user id

@app.route('/users/<int:id>', methods=['GET'])
def get_user_id(id):
    user = User.query.get(id)
    return jsonify(user.serialize()), 200

# characters

@app.route('/characters', methods=['GET', 'POST'])
def list_and_create_characters():

    if request.method == 'GET':
        characters = Characters.query.all()
        characters = list(
            map(lambda character: character.serialize(), characters))
        return jsonify(characters), 200

    if request.method == 'POST':
        data = request.get_json()

        character = Characters()
        character.name = data['name']
        character.height = data['height']
        character.mass = data['mass']
        character.eye_color = data['eye_color']
        character.birth_year = data['birth_year']
        character.gender = data['gender']
        character.image = data['image']

        character.save()

        return jsonify(character.serialize()), 201

# character by id

@app.route('/characters/<int:id>', methods=['GET'])
def character_by_id(id):
    character = Characters.query.get(id)
    return jsonify(character.serialize()), 200


# starships

@app.route('/starships', methods=['GET', 'POST'])
def list_and_create_starships():
    if request.method == 'GET':
        starships = Starships.query.all()
        starships = list(map(lambda starship: starship.serialize(), starships))
        return jsonify(starships), 200

    if request.method == 'POST':
        data = request.get_json()
        starship = Starships()

        starship.name = data['name']
        starship.model = data['model']
        starship.manufacturer = data['manufacturer']
        starship.cost_in_credits = data['cost_in_credits']
        starship.crew = data['crew']
        starship.passengers = data['passengers']
        starship.cargo_capacity = data['cargo_capacity']
        starship.length = data['length']
        starship.image = data['image']
        starship.save()

        return jsonify(starship.serialize()), 201

# starships by id

@app.route('/starships/<int:id>', methods=['GET'])
def starship_by_id(id):
    starship = Starships.query.get(id)
    return jsonify(starship.serialize()), 200


# planets

@app.route('/planets', methods=['GET', 'POST'])
def list_and_create_planets():

    if request.method == 'GET':
        planets = Planets.query.all()
        planets = list(map(lambda planet: planet.serialize(), planets))
        return jsonify(planets), 200

    if request.method == 'POST':
        data = request.get_json()
        planet = Planets()

        planet.name = data['name']
        planet.diameter = data['diameter']
        planet.climate = data['climate']
        planet.surface_water = data['surface_water']
        planet.population = data['population']
        planet.gravity = data['gravity']
        planet.image = data['image']

        planet.save()
        return jsonify(planet.serialize()), 201

# planets by id

@app.route('/planets/<int:id>', methods=['GET'])
def planet_by_id(id):
    planet = Planets.query.get(id)
    return jsonify(planet.serialize()), 200


#favorites 

@app.route('/users/favorites/', methods=['GET'])
def user_favorites():
    users = User.query.all()
    users = list(map(lambda user: user.serialize_favorites(), users))
    return jsonify(users), 200


# favorite characters add/delete

@app.route('/users/<int:user_id>/favorites/characters/<int:character_id>', methods=['POST', 'DELETE'])
def add_delete_characters(user_id, character_id):

    if request.method == 'POST':
        user = User.query.get(user_id)
        characters = Characters.query.get(character_id)

        user.fav_characters.append(characters)
        user.save()
        
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        favorite_character = user.fav_characters
        fav_character_filtered = filter(lambda character: character != Characters.query.get(character_id), favorite_character)
        user.fav_characters = list(fav_character_filtered)
        user.save()

    return jsonify({"user": user.serialize_favorites()}), 200

# favorite starships add/delete

@app.route('/users/<int:user_id>/favorites/starships/<int:starship_id>', methods=['POST', 'DELETE'])
def add_delete_starships(user_id, starship_id):

    if request.method == 'POST':
        user = User.query.get(user_id)
        starships = Starships.query.get(starship_id)

        user.fav_starships.append(starships)
        user.save()
        
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        favorite_starship = user.fav_starships
        fav_starship_filtered = filter(lambda starship: starship != Starships.query.get(starship_id), favorite_starship)
        user.fav_starships = list(fav_starship_filtered)
        user.save()

    return jsonify({"user": user.serialize_favorites()}), 200


# favorite planets add/delete

@app.route('/users/<int:user_id>/favorites/planets/<int:planet_id>', methods=['POST', 'DELETE'])
def add_delete_planets(user_id, planet_id):

    if request.method == 'POST':
        user = User.query.get(user_id)
        planets = Planets.query.get(planet_id)

        user.fav_planets.append(planets)
        user.save()
        
    if request.method == 'DELETE':
        user = User.query.get(user_id)
        favorite_planet = user.fav_planets
        fav_planet_filtered = filter(lambda planet: planet != Planets.query.get(planet_id), favorite_planet)
        user.fav_planets = list(fav_planet_filtered)
        user.save()

    return jsonify({"user": user.serialize_favorites()}), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    app.run()
