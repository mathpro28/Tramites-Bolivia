import React, { useState, useEffect, useRef } from 'react';
import './Chat.css';

const Chat = () => {
    const [messages, setMessages] = useState([
        { text: "Hello, how can I help you?", type: "bot" },
        { text: "I have a question about the services.", type: "user" },
        { text: "Sure, feel free to ask!", type: "bot" },
        // Add more messages as needed to simulate scrolling
    ]);

    const messagesEndRef = useRef(null);

    useEffect(() => {
        // Scroll to the bottom of the chat when a new message is added
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);

    const handleSendMessage = () => {
        // Example function to add new user messages
        setMessages([...messages, { text: "New message", type: "user" }]);
    };

    return (
        <div className="chat-window">
            <div className="chat-messages">
                {messages.map((msg, index) => (
                    <div
                        key={index}
                        className={`chat-message ${msg.type === "user" ? "user-message" : "bot-message"}`}
                    >
                        {msg.text}
                    </div>
                ))}
                <div ref={messagesEndRef} />
            </div>
            <div className="input-container">
                <textarea placeholder="Escribe tu consulta aquí..." rows="1" />
                <button onClick={handleSendMessage}>Send</button>
            </div>
        </div>
    );
};

export default Chat;
