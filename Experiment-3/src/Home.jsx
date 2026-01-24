
import React, { useState } from 'react';
import Button from './Button';
import TextField from './TextField';
import Checkbox from './Checkbox';
import Rating from './Rating';

export default function Home() {
  const [text, setText] = useState('');
  const [isChecked, setIsChecked] = useState(false);
  const [rating, setRating] = useState(0);

  const handleClick = () => {
    alert(`You entered: ${text}\nCheckbox: ${isChecked}\nRating: ${rating}`);
  };

  return (
    <div className="card">
      <h2>Experiment-3</h2>
      <TextField
        label="Enter Input"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Type something here..."
      />

      <div style={{ margin: '15px 0' }}>
        <Checkbox
          label="I agree to terms"
          checked={isChecked}
          onChange={(e) => setIsChecked(e.target.checked)}
        />
      </div>

      <div style={{ margin: '15px 0' }}>
        <p>Rate us:</p>
        <Rating
          value={rating}
          onChange={(newRating) => setRating(newRating)}
        />
      </div>

      <Button label="Submit" onClick={handleClick} />
    </div>
  );
}