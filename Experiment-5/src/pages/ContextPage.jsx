import React from 'react';
import ParentCounter from '../components/contextapi/CounterParent';

const ContextPage = () => {
    return (
        <div className="page-container">
            <h2>Global State (Context API)</h2>
            <p>Using React <code>Context</code> API.</p>
            <div className="component-wrapper">
                <ParentCounter cno="Counter 1" />
                <ParentCounter cno="Counter 2" />
            </div>
        </div>
    );
};

export default ContextPage;
