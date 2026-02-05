import { useDispatch, useSelector } from "react-redux";

export default function ListNotes() {
    const notes = useSelector((state) => state.note.notes);
    const dispatch = useDispatch();

    return (
        <div style={{ textAlign: "left", maxHeight: "200px", overflowY: "auto" }}>
            {notes.length === 0 ? (
                <p style={{ fontStyle: "italic", textAlign: "center" }}>No notes added yet.</p>
            ) : (
                <ul style={{ listStyle: "none", padding: 0 }}>
                    {notes.map((note) => (
                        <li
                            key={note.id}
                            style={{
                                background: "rgba(255,255,255,0.6)",
                                marginBottom: "8px",
                                padding: "8px",
                                borderRadius: "4px",
                                display: "flex",
                                justifyContent: "space-between",
                                alignItems: "center"
                            }}
                        >
                            <span>{note.text}</span>
                            <button
                                className="btn-delete"
                                onClick={() => dispatch({ type: "DELETE_NOTE", payload: note.id })}
                                style={{
                                    background: "transparent",
                                    color: "#d32f2f",
                                    border: "1px solid #d32f2f",
                                    padding: "4px 8px",
                                    marginLeft: "10px",
                                    fontSize: "0.75rem"
                                }}
                            >
                                Delete
                            </button>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
}
