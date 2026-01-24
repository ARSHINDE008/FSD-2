import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Home from './Home';
import About from './About';
import Contact from './Contact';

function App() {
    return (
        <div>
            <nav style={{ padding: '10px', marginBottom: '20px', borderBottom: '1px solid #ccc' }}>
                <Link to="/" style={{ marginRight: '10px' }}>Home</Link>
                <Link to="/about" style={{ marginRight: '10px' }}>About</Link>
                <Link to="/contact">Contact</Link>
            </nav>

            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
                <Route path="/contact" element={<Contact />} />
            </Routes>
        </div>
    );
}

export default App;
