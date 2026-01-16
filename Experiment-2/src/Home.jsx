
import React, { useState } from 'react';
import Button from './Button';
import TextField from './TextField';

export default function Home() {
  const [text, setText] = useState('');

  const handleClick = () => {
    alert(`You entered: ${text}`);
  };

  return (
    <div className="card">
      <h2>Experiment-2</h2>
      <TextField
        label="Enter Input"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type something here..."
      />
      <Button label="Submit" onClick={handleClick} />
    </div>
  );
}