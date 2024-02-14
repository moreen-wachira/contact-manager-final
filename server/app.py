from flask import Flask, request, jsonify, make_response,session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from sqlalchemy.exc import IntegrityError  # Import IntegrityError
from models import Contact, Address, PhoneNumber, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

migrate = Migrate(app, db)

db.init_app(app)

api=Api(app)

class Contacts(Resource):
    def post(self):
        data = request.json
        new_contact = Contact(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            birth_date=data.get('birth_date')
        )
        db.session.add(new_contact)
        db.session.commit()
        return {'message': 'Contact added successfully'}, 201

    def get(self):
        contacts = Contact.query.all()
        contacts_list = [{'id': contact.id, 'first_name': contact.first_name, 'last_name': contact.last_name,
                          'email': contact.email, 'birth_date': contact.birth_date} for contact in contacts]
        return contacts_list

    def put(self):
        data = request.json
        contact_id = data.get('id')
        contact = Contact.query.get(contact_id)
        if contact:
            contact.first_name = data.get('first_name', contact.first_name)
            contact.last_name = data.get('last_name', contact.last_name)
            contact.email = data.get('email', contact.email)
            contact.birth_date = data.get('birth_date', contact.birth_date)
            db.session.commit()
            return {'message': 'Contact updated successfully'}
        else:
            return {'error': 'Contact not found'}, 404

    def delete(self):
        data = request.json
        contact_id = data.get('id')
        contact = Contact.query.get(contact_id)
        if contact:
            db.session.delete(contact)
            db.session.commit()
            return {'message': 'Contact deleted successfully'}
        else:
            return {'error': 'Contact not found'}, 404

class ContactsByID(Resource):
    def post(self):
        data = request.json
        new_contact = Contact(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            birth_date=data.get('birth_date')
        )
        db.session.add(new_contact)
        db.session.commit()
        return {'message': 'Contact added successfully'}, 201

    def get(self, contact_id):
        contact = Contact.query.get(contact_id)
        if contact:
            return {'id': contact.id, 'first_name': contact.first_name, 'last_name': contact.last_name, 'email': contact.email, 'birth_date': contact.birth_date}
        else:
            return {'error': 'Contact not found'}, 404

    def put(self, contact_id):
        contact = Contact.query.get(contact_id)
        if contact:
            data = request.json
            contact.first_name = data.get('first_name', contact.first_name)
            contact.last_name = data.get('last_name', contact.last_name)
            contact.email = data.get('email', contact.email)
            contact.birth_date = data.get('birth_date', contact.birth_date)
            db.session.commit()
            return {'message': 'Contact updated successfully'}
        else:
            return {'error': 'Contact not found'}, 404

    def delete(self, contact_id):
        contact = Contact.query.get(contact_id)
        if contact:
            db.session.delete(contact)
            db.session.commit()
            return {'message': 'Contact deleted successfully'}
        else:
            return {'error': 'Contact not found'}, 404

class Addresses(Resource):
    def post(self):
        try:
            data = request.json
            new_address = Address(
                street=data['street'],
                city=data['city'],
                state=data['state'],
                contact_id=data['contact_id']
            )
            db.session.add(new_address)
            db.session.commit()
            return {'message': 'Address added successfully'}, 201
        except IntegrityError:
            db.session.rollback()
            return {'error': 'Invalid contact_id'}, 400
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500

    def get(self):
        addresses = Address.query.all()
        addresses_data = [{'id': address.id, 'street': address.street, 'city': address.city, 'state': address.state, 'contact_id': address.contact_id} for address in addresses]
        return make_response(jsonify(addresses_data),200)

    def put(self):
        data = request.json
        address_id = data.get('id')
        address = Address.query.get(address_id)
        if address:
            address.street = data.get('street', address.street)
            address.city = data.get('city', address.city)
            address.state = data.get('state', address.state)
            address.contact_id = data.get('contact_id', address.contact_id)
            db.session.commit()
            return {'message': 'Address updated successfully'}
        else:
            return {'error': 'Address not found'}, 404

    def delete(self):
        data = request.json
        address_id = data.get('id')
        address = Address.query.get(address_id)
        if address:
            db.session.delete(address)
            db.session.commit()
            return {'message': 'Address deleted successfully'}
        else:
            return {'error': 'Address not found'}, 404


class AddressesByID(Resource):
    def post(self):
        try:
            data = request.json
            new_address = Address(
                street=data['street'],
                city=data['city'],
                state=data['state'],
                contact_id=data['contact_id']
            )
            db.session.add(new_address)
            db.session.commit()
            return {'message': 'Address added successfully'}, 201
        except IntegrityError:
            db.session.rollback()
            return {'error': 'Invalid contact_id'}, 400
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500

    def get(self, address_id):
        address = Address.query.get(address_id)
        if address:
            return {'id': address.id, 'street': address.street, 'city': address.city, 'state': address.state, 'contact_id': address.contact_id}
        else:
            return {'error': 'Address not found'}, 404

    def put(self, address_id):
        address = Address.query.get(address_id)
        if address:
            data = request.json
            address.street = data.get('street', address.street)
            address.city = data.get('city', address.city)
            address.state = data.get('state', address.state)
            address.contact_id = data.get('contact_id', address.contact_id)
            db.session.commit()
            return {'message': 'Address updated successfully'}
        else:
            return {'error': 'Address not found'}, 404

    def delete(self, address_id):
        address = Address.query.get(address_id)
        if address:
            db.session.delete(address)
            db.session.commit()
            return {'message': 'Address deleted successfully'}
        else:
            return {'error': 'Address not found'}, 404


class PhoneNumbers(Resource):
    def post(self):
        try:
            data = request.json
            new_phone_number = PhoneNumber(
                number=data['number'],
                contact_id=data['contact_id']
            )
            db.session.add(new_phone_number)
            db.session.commit()
            return {'message': 'Phone number added successfully'}, 201
        except IntegrityError:
            db.session.rollback()
            return {'error': 'Invalid contact_id or duplicate phone number'}, 400
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500

    def get(self):
        phone_numbers = PhoneNumber.query.all()
        phone_numbers_data = [{'id': phone_number.id, 'number': phone_number.number, 'contact_id': phone_number.contact_id} for phone_number in phone_numbers]
        return make_response(jsonify(phone_numbers_data),200)

    def put(self):
        data = request.json
        phone_number_id = data.get('id')
        phone_number = PhoneNumber.query.get(phone_number_id)
        if phone_number:
            phone_number.number = data.get('number', phone_number.number)
            phone_number.contact_id = data.get('contact_id', phone_number.contact_id)
            db.session.commit()
            return {'message': 'Phone number updated successfully'}
        else:
            return {'error': 'Phone number not found'}, 404

    def delete(self):
        data = request.json
        phone_number_id = data.get('id')
        phone_number = PhoneNumber.query.get(phone_number_id)
        if phone_number:
            db.session.delete(phone_number)
            db.session.commit()
            return {'message': 'Phone number deleted successfully'}
        else:
            return {'error': 'Phone number not found'}, 404

class PhoneNumbersByID(Resource):
    def post(self):
        try:
            data = request.json
            new_phone_number = PhoneNumber(
                number=data['number'],
                contact_id=data['contact_id']
            )
            db.session.add(new_phone_number)
            db.session.commit()
            return {'message': 'Phone number added successfully'}, 201
        except IntegrityError:
            db.session.rollback()
            return {'error': 'Invalid contact_id or duplicate phone number'}, 400
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 500

    def get(self, phone_number_id):
        phone_number = PhoneNumber.query.get(phone_number_id)
        if phone_number:
            return {'id': phone_number.id, 'number': phone_number.number, 'contact_id': phone_number.contact_id}
        else:
            return {'error': 'Phone number not found'}, 404

    def put(self, phone_number_id):
        phone_number = PhoneNumber.query.get(phone_number_id)
        if phone_number:
            data = request.json
            phone_number.number = data.get('number', phone_number.number)
            phone_number.contact_id = data.get('contact_id', phone_number.contact_id)
            db.session.commit()
            return {'message': 'Phone number updated successfully'}
        else:
            return {'error': 'Phone number not found'}, 404

    def delete(self, phone_number_id):
        phone_number = PhoneNumber.query.get(phone_number_id)
        if phone_number:
            db.session.delete(phone_number)
            db.session.commit()
            return {'message': 'Phone number deleted successfully'}
        else:
            return {'error': 'Phone number not found'}, 404

api.add_resource(ContactsByID, '/contacts/<int:contact_id>')
api.add_resource(AddressesByID, '/addresses/<int:address_id>')
api.add_resource(PhoneNumbersByID, '/phonenumbers/<int:phone_number_id>')
api.add_resource(Contacts, '/contacts')
api.add_resource(Addresses, '/addresses')
api.add_resource(PhoneNumbers, '/phonenumbers')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
