// Warning.js
import React from 'react';
import './Warning.css'; // Create this CSS file for styling

const Warning = ({ message }) => {
  return (
    <div className="warning-container">
      <p>{message}</p>
    </div>
  );
};

export default Warning;
