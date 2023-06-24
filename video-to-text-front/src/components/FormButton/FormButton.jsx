import React from 'react';
import './FormButton.css';

export function FormButton({ children, className, disabled, ...props }) {
  return (
    <button {...props} className={className} type='submit' disabled={disabled}>
      {children}
    </button>
  );
}
