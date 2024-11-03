import React, { useState } from 'react';
import './MessageInput.css';

const MessageInput = ({ onSend }) => {
  const [message, setMessage] = useState('');

  const handleSend = () => {
    if (message.trim()) {
      onSend(message);
      setMessage(''); // Clear the input after sending
    }
  };

  return (
    <div className="message-input-container">
      <input
        type="text"
        className="message-input"
        placeholder="Type a message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)} // Update state on input change
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
      />
      <button onClick={handleSend} className="send-button">Send</button>
    </div>
  );
};

export default MessageInput;
