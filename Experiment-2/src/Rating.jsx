
import React from 'react';

const Rating = ({ value, max = 5, onChange }) => {
    return (
        <div>
            {[...Array(max)].map((_, index) => (
                <span
                    key={index}
                    onClick={() => onChange(index + 1)}
                    style={{
                        cursor: 'pointer',
                        fontSize: '24px',
                        color: index < value ? '#FFD700' : '#d3d3d3',
                    }}
                >
                    ★
                </span>
            ))}
        </div>
    );
};

export default Rating;
