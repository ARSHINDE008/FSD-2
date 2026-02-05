import { useDispatch, useSelector } from "react-redux";

export default function CounterReduxParent(props) {
  const count = useSelector(state => state.counter.count);
  const dispatch = useDispatch();

  return (
    <div className="counter-card card-orange">
      <h3>{props.cno} : Global State (Redux) Count: {count}</h3>

      <div className="btn-group">
        <button className="btn-white" onClick={() => dispatch({ type: "INCREMENT" })}>Increase</button>
        <button className="btn-white" onClick={() => dispatch({ type: "DECREMENT" })}>Decrease</button>
      </div>
    </div>
  );
}
