import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import './MessageWindow.css';

const MessageWindow = ({ messages }) => {
  const messageEndRef = useRef(null);

  useEffect(() => {
    if (messageEndRef.current) {
      messageEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  return (
    <div className="message-window">
      <h1 className="chat-title">¿Qué trámite haremos hoy?</h1>
      <div className="message-container">
        {messages.map((msg, index) => (
          msg.text.trim() && msg.sender && (
            <MessageBubble key={index} text={msg.text} sender={msg.sender} />
          )
        ))}
        {/* Add a div at the end to scroll to */}
        <div ref={messageEndRef} />
      </div>
    </div>
  );
};

export default MessageWindow;
