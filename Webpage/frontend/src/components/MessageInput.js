import React, { useState } from 'react';
import './MessageInput.css';
import Warning from './Warning';

const MessageInput = ({ onSend }) => {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');
  const [isSending, setIsSending] = useState(false);
  const MAX_MESSAGE_LENGTH = 500;

  const escapeHtml = (text) => {
    const div = document.createElement('div');
    div.appendChild(document.createTextNode(text));
    return div.innerHTML;
  };

  const handleSend = () => {
    if (message.trim() === '') {
      setError('Message cannot be empty.');
      return;
    } else if (message.length > MAX_MESSAGE_LENGTH) {
      setError(`Message cannot exceed ${MAX_MESSAGE_LENGTH} characters.`);
      return;
    }

    if (!isSending) {
      setIsSending(true);
      const sanitizedMessage = escapeHtml(message);
      onSend(sanitizedMessage);
      setMessage(''); // Clear the input after sending
      setError(''); // Clear any previous error message
      setTimeout(() => setIsSending(false), 1000); // Reset sending state after 1 second
    }
  };

  return (
    <div className="message-input-container">
      {error && <Warning message={error} />}
      <input
        type="text"
        className="message-input"
        placeholder="Type a message..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && handleSend()}
      />
      <button onClick={handleSend} className="send-button" disabled={isSending}>
        Send
      </button>
    </div>
  );
};

export default MessageInput;
