import React, { useState } from 'react';
import MessageWindow from './MessageWindow';
import axios from 'axios'; 
import './ChatWindow.css';

const ChatWindow = () => {
  // state for messages
  const [messages, setMessages] = useState([
    { text: '¡Hola! ¿Con qué tramite te puedo ayudar hoy?', sender: 'bot' }
  ]);

  // function to send messages to backend
  const sendMessage = async (text) => {
    const userMessage = { text, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      // request to API
      const response = await axios.post('http://127.0.0.1:5002/ask', {
        prompt: text
      });

      // add bot response
      const botMessage = { text: response.data.response, sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error al enviar la consulta:', error);
      const errorMessage = { text: 'Error al obtener respuesta del servidor.', sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
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
              const text = e.target.value.trim();
              if (text) {
                sendMessage(text); 
                e.target.value = ''; // clears input box
              }
            }
          }}
        />
        <button
          onClick={() => {
            const inputElement = document.querySelector('.message-input input');
            const text = inputElement.value.trim();
            if (text) {
              sendMessage(text); 
              inputElement.value = ''; // clears input box
            }
          }}
        >
          Enviar
        </button>
      </div>
    </div>
  );
};

export default ChatWindow;
