// ChatWindow.js
import React, { useState } from 'react';
import MessageBubble from './MessageBubble';
import MessageInput from './MessageInput';
import axios from 'axios'; // Importa axios
import './ChatWindow.css';

const ChatWindow = () => {
  const [messages, setMessages] = useState([{ text: "Hello! How can I help you today?", sender: "bot" }]);

  const addMessage = async (text) => {
    const userMessage = { text, sender: "user" };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      // Realiza la solicitud a la API
      const response = await axios.post('http://127.0.0.1:5000/ask', {
        prompt: text
      });

      // Agrega el mensaje del bot a la lista de mensajes
      const botMessage = { text: response.data.response, sender: "bot" };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error al enviar la consulta:', error);
      const errorMessage = { text: "Error al obtener respuesta del servidor.", sender: 'bot' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    }
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
