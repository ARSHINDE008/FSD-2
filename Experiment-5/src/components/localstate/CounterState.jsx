import { useState } from "react";

export default function LocalCounter(props) {
  const [count, setCount] = useState(0);

  // Event handler functions for click Event
  const increaseCount = () => setCount(count + 1);
  const decreaseCount = () => setCount(count - 1);

  return (
    <div className="counter-card card-blue">
      <h3>{props.cno} : Local State Count: {count}</h3>

      <div className="btn-group">
        <button className="btn-blue-solid" onClick={increaseCount}>INCREASE</button>
        <button className="btn-blue-outline" onClick={decreaseCount}>DECREASE</button>
      </div>
    </div>
  );
}