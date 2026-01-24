
import React from 'react';

const TextField = ({ label, value, onChange, placeholder }) => {
    return (
        <div className="input-group">
            <label className="input-label">{label}</label>
            <input
                type="text"
                className="input-field"
                value={value}
                onChange={onChange}
                placeholder={placeholder}
            />
        </div>
    );
};

export default TextField;
