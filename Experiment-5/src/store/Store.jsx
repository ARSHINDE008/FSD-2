import { createStore, combineReducers } from "redux";
import { CounterReducer } from "./CounterReducer.jsx";
import { NoteReducer } from "./NoteReducer.jsx";

const rootReducer = combineReducers({
    counter: CounterReducer, // Access state via state.counter.count
    note: NoteReducer        // Access state via state.note.notes
});

export const store = createStore(rootReducer);
