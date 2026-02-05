import React from 'react';
import LocalCounter from '../components/localstate/CounterState';

const LocalStatePage = () => {
    return (
        <div className="page-container">
            <h2>Local State Management</h2>
            <p>Using <code>useState</code> hook.</p>
            <div className="component-wrapper">
                <LocalCounter cno="Counter 1" />
                <LocalCounter cno="Counter 2" />
            </div>
        </div>
    );
};

export default LocalStatePage;
