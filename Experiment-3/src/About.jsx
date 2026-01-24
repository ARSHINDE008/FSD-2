
import React, { useState } from 'react';
import Select from './Select';
import Checkbox from './Checkbox';

export default function About() {
  const [selectedOption, setSelectedOption] = useState('option1');
  const [isPrimeMember, setIsPrimeMember] = useState(false);

  const options = [
    { label: 'Option 1', value: 'option1' },
    { label: 'Option 2', value: 'option2' },
    { label: 'Option 3', value: 'option3' },
  ];

  return (
    <div>
      <h2>About Page</h2>
      <Select
        label="Choose an option:"
        options={options}
        value={selectedOption}
        onChange={(e) => setSelectedOption(e.target.value)}
      />
      <p>Selected: {selectedOption}</p>
      <Checkbox
        label="I am a prime member"
        checked={isPrimeMember}
        onChange={(e) => setIsPrimeMember(e.target.checked)}
      />
      <p>Prime Member: {isPrimeMember ? 'Yes' : 'No'}</p>
    </div>
  );
}