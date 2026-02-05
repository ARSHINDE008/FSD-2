import React from 'react';
import CounterReduxParent from '../components/redux/CounterGlobalReduxParent';

const ReduxPage = () => {
    return (
        <div className="page-container">
            <h2>Global State (Redux)</h2>
            <p>Using <code>Redux</code> for state management.</p>
            <div className="component-wrapper">
                <CounterReduxParent cno="Counter 1" />
                <CounterReduxParent cno="Counter 2" />
            </div>
        </div>
    );
};

export default ReduxPage;
