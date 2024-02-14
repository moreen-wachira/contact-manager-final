import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const AddressesComponent = () => {
  const [addresses, setAddresses] = useState([]);
  const [newAddress, setNewAddress] = useState({
    street: '',
    city: '',
    state: '',
  });

  useEffect(() => {
    fetch('/addresses')
      .then((response) => response.json())
      .then((data) => {
        setAddresses(data);
      })
      .catch((error) => {
        console.error('Error fetching addresses:', error);
      });
  }, []);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewAddress((prevAddress) => ({
      ...prevAddress,
      [name]: value,
    }));
  };

  const handleCreateAddress = async () => {
    try {
      const response = await fetch('/addresses', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newAddress),
      });

      if (!response.ok) {
        throw new Error('Failed to create address');
      }

      const createdAddress = await response.json();
      setAddresses((prevAddresses) => [...prevAddresses, createdAddress]);
      setNewAddress({ street: '', city: '', state: '' });
    } catch (error) {
      console.error('Error creating address:', error);
    }
  };

  const handleDeleteAddress = async (id) => {
    try {
      const response = await fetch(`/addresses/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete address');
      }

      setAddresses((prevAddresses) =>
        prevAddresses.filter((address) => address.id !== id)
      );
    } catch (error) {
      console.error('Error deleting address:', error);
    }
  };

  return (
    <div>
      <h1>Addresses</h1>

      {/* Create Address Form */}
      <form>
        <label>
          Street:
          <input
            type="text"
            name="street"
            value={newAddress.street}
            onChange={handleInputChange}
          />
        </label>
        <label>
          City:
          <input
            type="text"
            name="city"
            value={newAddress.city}
            onChange={handleInputChange}
          />
        </label>
        <label>
          State:
          <input
            type="text"
            name="state"
            value={newAddress.state}
            onChange={handleInputChange}
          />
        </label>
        <button type="button" onClick={handleCreateAddress}>
          Create Address
        </button>
      </form>

      {/* List of Addresses */}
      <ul>
        {addresses.map((address) => (
          <li key={address.id}>
            <Link to={`/addresses/${address.id}`}>
              {address.street}, {address.city}, {address.state}
            </Link>
            <button onClick={() => handleDeleteAddress(address.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AddressesComponent;
