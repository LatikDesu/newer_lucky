import React from 'react';
import './InputTime.css';

export function InputTime({ children, id, ...props }) {
  const handleKeyDown = (event) => {
    const allowedChars = [
      '0',
      '1',
      '2',
      '3',
      '4',
      '5',
      '6',
      '7',
      '8',
      '9',
      ':',
      'Backspace',
      'ArrowRight',
      'Delete',
      'Tab',
    ];
    if (!allowedChars.includes(event.key)) {
      event.preventDefault();
    }
  };

  return (
    <input
      id={id}
      type='text'
      pattern='^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$'
      placeholder='00:00:00'
      onKeyDown={handleKeyDown}
      {...props}
    />
  );
}
