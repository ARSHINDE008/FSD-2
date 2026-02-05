import InputNote from "./InputNote";
import ListNotes from "./ListNotes";

export default function NoteWrapper() {
    return (
        <div className="counter-card card-purple">
            <h3>Note Module (Redux)</h3>
            <InputNote />
            <ListNotes />
        </div>
    );
}
