
import React from 'react';

const Select = ({ label, options, value, onChange }) => {
    return (
        <div style={{ marginBottom: '10px' }}>
            <label style={{ display: 'block', marginBottom: '5px' }}>{label}</label>
            <select value={value} onChange={onChange} style={{ padding: '8px', width: '100%' }}>
                {options.map((option, index) => (
                    <option key={index} value={option.value}>
                        {option.label}
                    </option>
                ))}
            </select>
        </div>
    );
};

export default Select;
