import './App.css'
import LocalCounter from "./components/CounterState";
import ParentCounter from "./components/CounterParent";
import CounterReduxParent from "./components/CounterGlobalReduxParent";

function App() {
  return (
    <div className="App">
      <LocalCounter />
      <ParentCounter />
      <ParentCounter />
      <CounterReduxParent cno="1" />
      <CounterReduxParent cno="2" />
    </div>
  )
}

export default App
