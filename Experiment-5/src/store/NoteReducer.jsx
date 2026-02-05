const initialState = {
  notes: []
};

export function NoteReducer(state = initialState, action) {
  switch (action.type) {
    case "ADD_NOTE":
      return {
        notes: [...state.notes, { id: Date.now(), text: action.payload }]
      };

    case "DELETE_NOTE":
      return {
        notes: state.notes.filter((note) => note.id !== action.payload)
      };

    default:
      return state;
  }
}
