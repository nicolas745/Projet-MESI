import React from 'react';
import './Navbar.css';

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="logo">Logo</div>
      <div className="profile">
        <img src="/logo192.png" alt="Photo de profil" />
        <span>Melvine</span>
      </div>
    </nav>
  );
}

export default Navbar;
