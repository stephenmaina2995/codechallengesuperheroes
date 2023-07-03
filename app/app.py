#!/usr/bin/env python3

# from flask import Flask, make_response, jsonify, request
# from flask_migrate import Migrate
# from models import db, Hero, Power, HeroPower
# # from marshmallow import fields

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/app.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# migrate = Migrate(app, db)
# db.init_app(app)

# hero_schema = HeroSchema()
# heroes_schema = HeroSchema(many=True)

# # @app.route('/')
# # def home():
# #     return 'hello world'

# @app.route('/heroes', methods=['GET'])
# def get_heroes():
#     heroes = Hero.query.all()
#     result = heroes_schema.dump(heroes)
#     return jsonify(result)

# @app.route('/heroes/<id>/', methods=['GET'])
# def post_hero(id):
#     hero = Hero.query.get(id)
#     return heroes_schema.jsonify(hero)

# @app.route('/powers', methods=['GET'])
# def get_powers():
#     powers = powers.query.all()
#     result = powers_schema.dump(powers)
#     return jsonify(result)

# @app.route('/powers/<id>/', methods=['GET'])
# def post_powers(id):
#     powers = powers.query.get()
#     return powers_schema.jsonify(powers)

# @app.route('/powers/<id>/', methods=['PATCH'])
# def update_hero(id):
#     powers = powers.query.get(id)

#     name = request.json['name']
#     description = request.json['description']

#     powers.name = name
#     powers.description = description

#     db.session.commit()
#     return powers_schema.jsonify(powers)
   
# @app.route('/hero_powers', methods=['POST'])
# def add_hero():
#     data = request.get_json()
#     id = data['id']
#     hero_powers = data['hero_powers']
#     hero = Hero(id=id, hero_powers=hero_powers)
#     db.session.add(hero)
#     db.session.commit()
#     return hero.jsonify(hero)

# if __name__ == '__main__':
#     app.run(port=5555)
from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    result = []
    for hero in Hero.query.all():
        hero = {
            "id" : hero.id,
            "name": hero.name, 
            "super_name": hero.super_name
            }
        result.append(hero)
    return jsonify(result)

@app.route('/heroes/<id>/', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero)
    else:
        return jsonify({'message': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    result = []
    for power in powers:
        power={
            "id": power.id,
        "name": power.name,
        "description": power.description,
        "created_at": power.created_at,
        "updated_at" : power.updated_at
        }
        result.append(power)
    return jsonify(result)

@app.route('/powers/<id>/', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.to_dict())
    else:
        return jsonify({'message': 'Power not found'}), 404

@app.route('/powers/<id>/', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        name = request.json.get('name')
        description = request.json.get('description')

        if name is not None:
            power.name = name
        if description is not None:
            power.description = description

        db.session.commit()
        return jsonify(power)
    else:
        return jsonify({'message': 'Power not found'}), 404

@app.route('/hero_powers', methods=['POST'])
def add_hero():
    data = request.form
    

    # if id is not None and hero_powers is not None:
    hero = HeroPower(
        strength = data.get('strength'),
        power_id = data.get('power_id'),
        hero_id = data.get('hero_id')
        
        
        )
    db.session.add(hero)
    db.session.commit()
    return jsonify(hero)
    # else:
    #     return jsonify({'message': 'Invalid request'}), 400

if __name__ == '__main__':
    app.run(port=5555)
    # seed_database()
