
import React, { useState } from 'react';
import Rating from './Rating';

export default function Contact() {
  const [rating, setRating] = useState(0);

  return (
    <div>
      <h2>Contact Page</h2>
      <p>Rate us:</p>
      <Rating value={rating} onChange={setRating} />
      <p>Your rating: {rating} stars</p>
    </div>
  );
}