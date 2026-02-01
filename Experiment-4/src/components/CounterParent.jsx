import { useContext } from "react";
import { CounterContext } from "./CounterContextApi";

function ParentCounter() {
    const { count, setCount } = useContext(CounterContext);

    return (
        <div style={{ backgroundColor: "#dcfce7", padding: "20px", margin: "10px", borderRadius: "8px", textAlign: "center" }}>
            <h3>1 : Gloabl State (ContextAPI) Count: {count}</h3>

            <button onClick={() => setCount(count + 1)} style={{ margin: "5px", padding: "10px 20px", backgroundColor: "transparent", color: "#15803d", border: "1px solid #15803d", borderRadius: "4px", cursor: "pointer" }}>
                INCREASE
            </button>

            <button onClick={() => setCount(count - 1)} style={{ margin: "5px", padding: "10px 20px", backgroundColor: "transparent", color: "#15803d", border: "1px solid #15803d", borderRadius: "4px", cursor: "pointer" }}>
                DECREASE
            </button>
        </div>
    );
}

export default ParentCounter;
