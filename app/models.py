# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import CheckConstraint
# from sqlalchemy.orm import validates

# db = SQLAlchemy()

# class Hero(db.Model):
#     __tablename__ = 'hero'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     super_name = db.Column(db.String)
#     created_at = db.Column(db.Date)
#     updated_at = db.Column(db.Date)
#     hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

# class Power(db.Model):
#     __tablename__ = 'power'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)

#     @validates('description')
#     def validate_description(self, key, description):
#         if len(description) < 20:
#             raise ValueError('Description must be at least 20 characters long.')
#         return description

#     hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

# class HeroPower(db.Model):
#     __tablename__ = 'hero_power'

#     id = db.Column(db.Integer, primary_key=True)
#     # strength = db.Column(db.String(255), db.ForeignKey)
#     hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
#     power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
#     strength = db.Column(db.String(50), nullable=False)
#     created_at = db.Column(db.Date)
#     updated_at = db.Column(db.Date)

#     @validates('strength')
#     def validate_strength(self, key, strength):
#         allowed_strengths = ['Strong', 'Weak', 'Average']
#         if strength not in allowed_strengths:
#             raise ValueError('Strength must be one of the following: Strong, Weak, Average.')
#         return strength

    # __table_args__ = (
    #     CheckConstraint(strength.in_(allowed_strengths), name='valid_strength_check'),
    # )
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import validates

# db = SQLAlchemy()

# class Hero(db.Model):
#     __tablename__ = 'hero'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     super_name = db.Column(db.String)
#     created_at = db.Column(db.Date)
#     updated_at = db.Column(db.Date)
#     hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

#     def to_dict(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'super_name': self.super_name,
#             'created_at': self.created_at,
#             'updated_at': self.updated_at,
#             'hero_powers': [hero_power.to_dict() for hero_power in self.hero_powers]
#         }

# class Power(db.Model):
#     __tablename__ = 'power'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     description = db.Column(db.String(255), nullable=False)
#     created_at = db.Column(db.DateTime)
#     updated_at = db.Column(db.DateTime)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    super_name = db.Column(db.String)
    created_at = db.Column(db.Date)
    updated_at = db.Column(db.Date)
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'hero_powers': [hero_power.to_dict() for hero_power in self.hero_powers]
        }


class Power(db.Model):
    __tablename__ = 'power'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), primary_key=True)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), primary_key=True)
    strength = db.Column(db.String(255))

    hero = db.relationship('Hero', backref=db.backref('hero_powers', cascade='all, delete-orphan'))
    power = db.relationship('Power', backref=db.backref('power_heroes', cascade='all, delete-orphan'))

    def to_dict(self):
        return {
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength
        }
