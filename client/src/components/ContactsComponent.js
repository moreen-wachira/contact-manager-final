import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
// import './ContactsComponent.css';

const ContactsComponent = () => {
  const [contacts, setContacts] = useState([]);
  const [newContact, setNewContact] = useState({
    first_name: '',
    last_name: '',
    email: '',
  });

  useEffect(() => {
    fetch('/contacts')
      .then((response) => response.json())
      .then((data) => {
        setContacts(data);
      })
      .catch((error) => {
        console.error('Error fetching contacts:', error);
      });
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewContact((prevContact) => ({
      ...prevContact,
      [name]: value,
    }));
  };

  const handleCreateContact = async () => {
    try {
      const response = await fetch('/contacts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newContact),
      });

      if (!response.ok) {
        throw new Error('Failed to create contact');
      }

      const createdContact = await response.json();
      setContacts((prevContacts) => [...prevContacts, createdContact]);
      setNewContact({ first_name: '', last_name: '', email: '' });
    } catch (error) {
      console.error('Error creating contact:', error);
    }
  };

  const handleDeleteContact = async (id) => {
    try {
      const response = await fetch(`/contacts/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete contact');
      }

      setContacts((prevContacts) =>
        prevContacts.filter((contact) => contact.id !== id)
      );
    } catch (error) {
      console.error('Error deleting contact:', error);
    }
  };

  return (
    <div>
      <h1>Contacts</h1>

      {/* Create Contact Form */}
      <form>
        <label>
          First Name:
          <input
            type="text"
            name="first_name"
            value={newContact.first_name}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Last Name:
          <input
            type="text"
            name="last_name"
            value={newContact.last_name}
            onChange={handleInputChange}
          />
        </label>
        <label>
          Email:
          <input
            type="text"
            name="email"
            value={newContact.email}
            onChange={handleInputChange}
          />
        </label>
        <button type="button" onClick={handleCreateContact}>
          Create Contact
        </button>
      </form>

      {/* List of Contacts */}
      <ul>
        {contacts.map((contact) => (
          <li key={contact.id}>
            <Link to={`/contacts/${contact.id}`}>
              {contact.first_name} {contact.last_name}
            </Link>
            <button onClick={() => handleDeleteContact(contact.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ContactsComponent;
