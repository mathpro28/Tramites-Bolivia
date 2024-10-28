import React, { useState } from 'react';
import MessageBubble from './MessageBubble';
import MessageInput from './MessageInput';
import './ChatWindow.css';

const ChatWindow = () => {
  const [messages, setMessages] = useState([{ text: "Hello! How can I help you today?", sender: "bot" }]);

  const addMessage = (text) => {
    setMessages([...messages, { text, sender: "user" }]);
  };

  return (
    <div className="chat-window">
      <div className="message-list">
        {messages.map((msg, index) => (
          <MessageBubble key={index} text={msg.text} sender={msg.sender} />
        ))}
      </div>
      <MessageInput onSend={addMessage} />
    </div>
  );
};

export default ChatWindow;
