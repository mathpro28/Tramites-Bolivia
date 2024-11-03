import React from 'react';
import MessageBubble from './MessageBubble';
import './MessageWindow.css';

const MessageWindow = ({ messages }) => (
  <div className="message-window">
    <h1 className="chat-title">¿Qué tramite haremos hoy?</h1>
    <div className="message-container">
      {messages.map((msg, index) => (
        <MessageBubble key={index} text={msg.text} sender={msg.sender} />
      ))}
    </div>
  </div>
);

export default MessageWindow;
