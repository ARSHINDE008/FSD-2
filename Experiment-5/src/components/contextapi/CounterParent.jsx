import { useContext } from "react";
import { CounterContext } from "./CounterContextApi";

function ParentCounter(props) {
  const { count, setCount } = useContext(CounterContext);

  return (
    <div className="counter-card card-green">
      <h3>{props.cno} : Global State (ContextAPI) Count: {count}</h3>

      <div className="btn-group">
        <button className="btn-green-outline" onClick={() => setCount(count + 1)}>
          INCREASE
        </button>

        <button className="btn-green-outline" onClick={() => setCount(count - 1)}>
          DECREASE
        </button>
      </div>
    </div>
  );
}

export default ParentCounter;