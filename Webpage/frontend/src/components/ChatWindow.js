import React, { useState } from 'react';
import MessageWindow from './MessageWindow';
import axios from 'axios'; // Importa axios para la conexión al backend
import './ChatWindow.css';

const ChatWindow = () => {
  // Estado para mantener los mensajes
  const [messages, setMessages] = useState([
    { text: '¡Hola! ¿Con qué tramite te puedo ayudar hoy?', sender: 'bot' }
  ]);

  // Función para agregar un nuevo mensaje y enviar al backend
  const sendMessage = async (text) => {
    const userMessage = { text, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);

    try {
      // Realiza la solicitud a la API
      const response = await axios.post('http://127.0.0.1:5002/ask', {
        prompt: text
      });

      // Agrega la respuesta del bot al estado de los mensajes
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
                sendMessage(text); // Llama a la función para enviar el mensaje
                e.target.value = ''; // Limpia el campo de entrada
              }
            }
          }}
        />
        <button
          onClick={() => {
            const inputElement = document.querySelector('.message-input input');
            const text = inputElement.value.trim();
            if (text) {
              sendMessage(text); // Llama a la función para enviar el mensaje
              inputElement.value = ''; // Limpia el campo de entrada
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
