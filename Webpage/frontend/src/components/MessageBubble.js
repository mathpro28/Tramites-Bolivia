import React from 'react';
import './MessageBubble.css';

const MessageBubble = ({ text, sender }) => (
  <div className={`message-bubble ${sender}`}>
    <img src={sender === 'bot' ? '/bot-icon.png' : '/user-icon.png'} alt="icon" className="avatar" />
    <p className="message-text">{text}</p>
  </div>
);

export default MessageBubble;
