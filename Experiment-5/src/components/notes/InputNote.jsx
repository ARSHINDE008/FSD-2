import { useState } from "react";
import { useDispatch } from "react-redux";

export default function InputNote() {
    const [text, setText] = useState("");
    const dispatch = useDispatch();

    const handleAdd = () => {
        if (text.trim()) {
            dispatch({ type: "ADD_NOTE", payload: text });
            setText("");
        }
    };

    return (
        <div style={{ marginBottom: "20px" }}>
            <input
                type="text"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Enter note..."
                style={{
                    padding: "8px",
                    borderRadius: "4px",
                    border: "1px solid #ccc",
                    marginRight: "10px",
                    width: "60%"
                }}
            />
            <button className="btn-purple-solid" onClick={handleAdd}>
                Add Note
            </button>
        </div>
    );
}
