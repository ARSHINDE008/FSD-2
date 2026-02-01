import { useState } from "react";

export default function LocalCounter() {
    const [count, setCount] = useState(0);

    // Event handler functions for click Event
    const increaseCount = () => setCount(count + 1);
    const decreaseCount = () => setCount(count - 1);

    return (
        <div style={{ backgroundColor: "#dbeafe", padding: "20px", margin: "10px", borderRadius: "8px", textAlign: "center" }}>

            <h3>2 : Local State Count: {count}</h3>
            {/* Binding event handlers to buttons  */}
            <button onClick={increaseCount} style={{ margin: "5px", padding: "10px 20px", backgroundColor: "#1d4ed8", color: "white", border: "none", borderRadius: "4px", cursor: "pointer" }}>
                INCREASE
            </button>

            <button onClick={decreaseCount} style={{ margin: "5px", padding: "10px 20px", backgroundColor: "#dbeafe", color: "#1d4ed8", border: "1px solid #1d4ed8", borderRadius: "4px", cursor: "pointer" }}>
                DECREASE
            </button>

        </div>
    );
}
