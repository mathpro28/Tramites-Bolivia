import React from 'react';
import ChatHeader from './Components/ChatHeader';
import ChatSidebar from './Components/ChatSidebar';
import ChatWindow from './Components/ChatWindow';
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
