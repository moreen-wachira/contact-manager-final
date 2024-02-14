import React from 'react';
import { Routes, Route, } from 'react-router-dom';
import ContactsComponent from './components/ContactsComponent';
import AddressesComponent from './components/AddressesComponent';
import PhoneNumbersComponent from './components/PhoneNumbersComponent';
import Navbar from './components/NavBar';
import Home from './components/Home';

// import ContactsByIDComponent from './ContactsByIDComponent';
// import AddressesByIDComponent from './AddressesByIDComponent';
// import PhoneNumbersByIDComponent from './PhoneNumbersByIDComponent';

const App = () => {
  return (<><Navbar/>
    <Routes>
      
      {/* <div>
        <Switch> */}
          {/* <Route path="/contacts/:contact_id" component={ContactsByIDComponent} />
          <Route path="/addresses/:address_id" component={AddressesByIDComponent} />
          <Route path="/phonenumbers/:phone_number_id" component={PhoneNumbersByIDComponent} */}
          <Route path="/contacts" element={<ContactsComponent/>} />
          <Route path="/addresses" element={<AddressesComponent/>} />
          <Route path="/phonenumbers" element={<PhoneNumbersComponent/>} />
          <Route path="/" element={<Home/>} />

          {/* Add a default route or handle 404 */}
        {/* </Switch>
      </div> */}
    </Routes>
    </>
  );
};

export default App;
