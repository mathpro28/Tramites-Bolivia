import React, { useState } from 'react';
import MessageBubble from './MessageBubble';
import MessageInput from './MessageInput';
import axios from 'axios'; // Importa axios
import MessageWindow from './MessageWindow';
import './ChatWindow.css';
//¿Cuál es la URL del sitio web de la organización Ministerio de Educación de Bolivia?
const ChatWindow = () => {
  // Example state to hold chat messages
  const [messages, setMessages] = useState([
    { text: '¡Hola! ¿Con qué tramite te puedo ayudar hoy?', sender: 'bot' },
    { text: 'I want to learn more about your services.', sender: 'user' }
  ]);

  const sendMessage = async (text) => {
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
