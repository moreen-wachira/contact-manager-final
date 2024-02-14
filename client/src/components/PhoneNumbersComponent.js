import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
// import './PhoneNumbersComponent.css';

const PhoneNumbersComponent = () => {
  const [phoneNumbers, setPhoneNumbers] = useState([]);
  const [newPhoneNumber, setNewPhoneNumber] = useState('');

  useEffect(() => {
    fetch('/phonenumbers')
      .then((response) => response.json())
      .then((data) => {
        setPhoneNumbers(data);
      })
      .catch((error) => {
        console.error('Error fetching phone numbers:', error);
      });
  }, []);

  const handleInputChange = (e) => {
    e.preventDefault()
    console.log(newPhoneNumber)
    try {
       fetch('/phonenumbers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newPhoneNumber),
      }); 
    }
    catch {}
    // const { name, value } = e.target;
    // setNewPhoneNumber((prevPhoneNumber) => ({
    //   ...prevPhoneNumber,
    //   [name]: value,
    // }));
  };

  const handleCreatePhoneNumber = async () => {
    try {
      const response = await fetch('/phonenumbers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newPhoneNumber),
      });

      if (!response.ok) {
        throw new Error('Failed to create phone number');
      }

      const createdPhoneNumber = await response.json();
      setPhoneNumbers((prevPhoneNumbers) => [
        ...prevPhoneNumbers,
        createdPhoneNumber,
      ]);
      setNewPhoneNumber({ number: '' });
    } catch (error) {
      console.error('Error creating phone number:', error);
    }
  };

  const handleDeletePhoneNumber = async (id) => {
    try {
      const response = await fetch(`/phonenumbers/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete phone number');
      }

      setPhoneNumbers((prevPhoneNumbers) =>
        prevPhoneNumbers.filter((phoneNumber) => phoneNumber.id !== id)
      );
    } catch (error) {
      console.error('Error deleting phone number:', error);
    }
  };

  return (
    <div>
      <h1>Phone Numbers</h1>

      {/* Create Phone Number Form */}
      <form onSubmit={handleInputChange}>
        <label>
          Number:
          <input
            type="number"
            name="number"
            value={newPhoneNumber}
            onChange={(e) => setNewPhoneNumber(e.target.value)}
          />
        </label>
        {/* <button type="button" onClick={handleCreatePhoneNumber}>
          Create Phone Number
        </button> */}
        <input 
        type = "submit"/>

      </form>

      {/* List of Phone Numbers */}
      <ul>
        {phoneNumbers.map((phoneNumber) => (
          <li key={phoneNumber.id}>
            <Link to={`/phone_numbers/${phoneNumber.id}`}>
              {phoneNumber.number}
            </Link>
            <button onClick={() => handleDeletePhoneNumber(phoneNumber.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PhoneNumbersComponent;
