import React from 'react';
import './ChatHeader.css';
import leftImage from '../assets/images/bolivian-logo.png';  // Update path as needed
import rightImage from '../assets/images/upb-logo.jpeg'; // Update path as needed

const ChatHeader = () => (
  <div className="chat-header">
    <div className="header-content">
      <img src={leftImage} alt="Left logo" className="header-image" />
      <div className="header-text">
        <h1>TramiBot AI Bolivia</h1>
        <p>Hacer <strong>tramites</strong> en Bolivia no tiene que ser tan <strong>feo</strong></p>
      </div>
      <img src={rightImage} alt="Right logo" className="header-image" />
    </div>
  </div>
);

export default ChatHeader;
