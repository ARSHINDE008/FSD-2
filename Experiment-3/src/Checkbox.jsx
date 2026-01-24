
import React from 'react';

const Checkbox = ({ label, checked, onChange }) => {
    return (
        <div style={{ marginBottom: '10px' }}>
            <label style={{ display: 'flex', alignItems: 'center' }}>
                <input
                    type="checkbox"
                    checked={checked}
                    onChange={onChange}
                    style={{ marginRight: '10px' }}
                />
                {label}
            </label>
        </div>
    );
};

export default Checkbox;
