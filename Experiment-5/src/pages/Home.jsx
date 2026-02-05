import React from 'react';

const Home = () => {
    return (
        <div className="page-container home-page">
            <h1>Experiment 5: Lazy Loading Optimization</h1>
            <p>
                This application demonstrates performance optimization using <strong>React.lazy</strong> and <strong>Suspense</strong> with <strong>React Router</strong>.
            </p>
            <div className="features">
                <div className="feature-card">
                    <h3>Code Splitting</h3>
                    <p>Components are split into separate bundles and loaded only when needed.</p>
                </div>
                <div className="feature-card">
                    <h3>Suspense</h3>
                    <p>Displays a graceful loading state while code chunks are being fetched.</p>
                </div>
                <div className="feature-card">
                    <h3>Routing</h3>
                    <p>Each major feature has its own route, enabling efficient page-level loading.</p>
                </div>
            </div>
        </div>
    );
};

export default Home;
