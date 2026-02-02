import React from 'react';
import { Link } from 'react-router-dom';
import '../styles/Navbar.css';

function Navbar({ isLoggedIn }) {
  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          🎾 <span>Tennis Match Predictor</span>
        </Link>
        
        <div className="nav-menu">
          <Link to="/" className="nav-item">Home</Link>
          {!isLoggedIn ? (
            <div className="auth-buttons">
              <Link to="/login" className="nav-item">Login</Link>
              <Link to="/register" className="nav-item btn-primary">Register</Link>
            </div>
          ) : (
            <Link to="/logout" className="nav-item btn-logout">Logout</Link>
          )}
        </div>
      </div>
    </nav>
  );
}

export default Navbar;