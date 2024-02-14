// Navbar.js
import React from 'react';
import { NavLink } from 'react-router-dom';
import './NavBar.css'; // Import the CSS file

const Navbar = () => {
  return (
    <nav>
      <ul>
        <li>
          <NavLink to="/" exact activeClassName="active">
            Home
          </NavLink>
        </li>
        <li>
          <NavLink to="/contacts" activeClassName="active">
            Contacts
          </NavLink>
        </li>
        <li>
          <NavLink to="/phonenumbers" activeClassName="active">
            Phone Numbers
          </NavLink>
        </li>
        <li>
          <NavLink to="/addresses" activeClassName="active">
            Addresses
          </NavLink>
        </li>
      </ul>
    </nav>
  );
};

export default Navbar;
