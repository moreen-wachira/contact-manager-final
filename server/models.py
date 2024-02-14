from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Contact(db.Model, SerializerMixin):
    __tablename__ = 'contacts'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    birth_date = db.Column(db.String)
    addresses = db.relationship('Address', backref='contact', lazy=True, cascade='all, delete-orphan')
    phone_numbers = db.relationship('PhoneNumber', backref='contact', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f"Contact(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"

class Address(db.Model, SerializerMixin):
    __tablename__ = 'addresses'

    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)

    def __repr__(self):
        return f"Address(id={self.id}, street='{self.street}', city='{self.city}', state='{self.state}')"

class PhoneNumber(db.Model, SerializerMixin):
    __tablename__ = 'phone_numbers'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), nullable=False)
    contact_id = db.Column(db.Integer, db.ForeignKey('contacts.id'), nullable=False)

    def __repr__(self):
        return f"PhoneNumber(id={self.id}, number='{self.number}')"
