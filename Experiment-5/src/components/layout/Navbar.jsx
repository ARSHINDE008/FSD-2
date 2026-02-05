import React from 'react';
import { NavLink } from 'react-router-dom';

const Navbar = () => {
    return (
        <nav className="navbar">
            <div className="nav-container">
                <div className="logo">Experiment 5</div>
                <ul className="nav-links">
                    <li>
                        <NavLink to="/" className={({ isActive }) => (isActive ? 'active' : '')}>
                            Home
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/local" className={({ isActive }) => (isActive ? 'active' : '')}>
                            Local State
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/context" className={({ isActive }) => (isActive ? 'active' : '')}>
                            Context API
                        </NavLink>
                    </li>
                    <li>
                        <NavLink to="/redux" className={({ isActive }) => (isActive ? 'active' : '')}>
                            Redux
                        </NavLink>
                    </li>
                </ul>
            </div>
        </nav>
    );
};

export default Navbar;
