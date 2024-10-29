import React from 'react';
import './ChatSidebar.css';

const tools = [
  { name: 'Licencia de Conducir' },
  { name: 'Certificado Legalizado' },
  { name: 'Titulo Bachiller' },
  { name: 'Certificado Solteria' },
];

const characters = [
  { name: 'SEDUCA' },
  { name: 'SEGIP' },
  { name: 'SEREPI' },
];

const ChatSidebar = () => (
  <div className="chat-sidebar">
    <h3>Tramites</h3>
    <ul>
      {tools.map((tool, index) => (
        <li key={index}>{tool.name}</li>
      ))}
    </ul>
    <h3>Instituciones</h3>
    <ul>
      {characters.map((character, index) => (
        <li key={index}>{character.name}</li>
      ))}
    </ul>
  </div>
);

export default ChatSidebar;
