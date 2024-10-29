import React from 'react';
import ChatHeader from './components/ChatHeader';
import ChatSidebar from './components/ChatSidebar';
import ChatWindow from './components/ChatWindow';
import './App.css';

function App() {
  return (
    <div className="app-container">
      <ChatHeader />
      <div className="app-body">
        <ChatSidebar />
        <ChatWindow />
      </div>
    </div>
  );
}

export default App;
