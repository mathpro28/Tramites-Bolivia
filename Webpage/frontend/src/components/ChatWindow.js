import React, { useState } from 'react';
import MessageWindow from './MessageWindow';
import './ChatWindow.css';

const ChatWindow = () => {
  // Example state to hold chat messages
  const [messages, setMessages] = useState([
    { text: '¡Hola! ¿Con qué tramite te puedo ayudar hoy?', sender: 'bot' },
    { text: 'I want to learn more about your services.', sender: 'user' }
  ]);

  // Function to add a new message
  const sendMessage = (text) => {
    setMessages([...messages, { text, sender: 'user' }]);
  };

  return (
    <div className="chat-window">
      <MessageWindow messages={messages} />
      <div className="message-input">
        <input
          type="text"
          placeholder="Escribe tu consulta aquí..."
          onKeyDown={(e) => {
            if (e.key === 'Enter') {
              sendMessage(e.target.value);
              e.target.value = ''; // Clear input field
            }
          }}
        />
        <button onClick={() => sendMessage(document.querySelector('.message-input input').value)}>
          Send
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;
