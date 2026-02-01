import { useDispatch, useSelector } from "react-redux"; //npm install redux react-redux

export default function CounterReduxParent(props) {
    // useSelector : to read state from the Redux store
    const count = useSelector(state => state.count);

    // useDispatch : to dispatch actions to the Redux store
    const dispatch = useDispatch();

    return (
        <div style={{ backgroundColor: "#ffedd5", padding: "20px", margin: "10px", borderRadius: "8px", textAlign: "center" }}>
            <h3>{props.cno} : Gloabl State (Redux) Count: {count}</h3>

            <button onClick={() => dispatch({ type: "INCREMENT" })} style={{ margin: "5px", padding: "10px 20px", backgroundColor: "white", color: "black", border: "none", borderRadius: "4px", cursor: "pointer", fontWeight: "bold" }}>
                Increase
            </button>

            <button onClick={() => dispatch({ type: "DECREMENT" })} style={{ margin: "5px", padding: "10px 20px", backgroundColor: "white", color: "black", border: "none", borderRadius: "4px", cursor: "pointer", fontWeight: "bold" }}>
                Decrease
            </button>
        </div>
    );
}
