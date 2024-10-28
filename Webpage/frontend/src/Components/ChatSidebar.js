import React from 'react';
import './ChatSidebar.css';

const tools = [
  { name: 'Paragraph Writer' },
  { name: 'Essay Writer' },
  { name: 'Text Summarizer' },
  { name: 'AI Text Rewriter' },
];

const characters = [
  { name: 'Luna' },
  { name: 'Sofia' },
  { name: 'Ethan' },
];

const ChatSidebar = () => (
  <div className="chat-sidebar">
    <h3>Tools</h3>
    <ul>
      {tools.map((tool, index) => (
        <li key={index}>{tool.name}</li>
      ))}
    </ul>
    <h3>Characters</h3>
    <ul>
      {characters.map((character, index) => (
        <li key={index}>{character.name}</li>
      ))}
    </ul>
  </div>
);

export default ChatSidebar;
