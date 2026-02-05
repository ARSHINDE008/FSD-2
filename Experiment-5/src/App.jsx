import { Suspense, lazy } from 'react';
import Loading from './components/ui/Loading';

// Lazy load the components
const LocalCounter = lazy(() => import('./components/localstate/CounterState'));
const ParentCounter = lazy(() => import('./components/contextapi/CounterParent')); // Also lazy loading this for consistency
const CounterReduxParent = lazy(() => import('./components/redux/CounterGlobalReduxParent'));

const NoteWrapper = lazy(() => import('./components/notes/NoteWrapper'));

function App() {
  return (
    <div className="app-container">
      <h1 style={{ textAlign: 'center', marginTop: '20px' }}>Experiment 5: Lazy Loading</h1>
      <h3 style={{ textAlign: 'center', color: '#666' }}>23bis70049-ARSHINDER SINGH</h3>


      <main className="main-content" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
        <Suspense fallback={<Loading />}>

          {/* Section 1: Local State - Blue */}
          <LocalCounter cno="2" />

          {/* Section 2: Context API - Green */}
          <ParentCounter cno="1" />
          <ParentCounter cno="1" />

          {/* Section 3: Redux - Orange */}
          <CounterReduxParent cno="1" />
          <CounterReduxParent cno="2" />

          {/* Section 4: Notes - Purple */}
          <NoteWrapper />

        </Suspense>
      </main>
    </div>
  );
}

export default App;
