import React from 'react';
import './ChatSidebar.css';

const tools = [
  { name: 'Licencia de Conducir' },
  { name: 'Certificado Legalizado' },
  { name: 'Titulo Bachiller' },
  { name: 'Certificado Solteria' },
];

const institutions = [
  { name: 'SEDUCA' },
  { name: 'SEGIP' },
  { name: 'SEREPI' },
];

const additionalServices = [
  { name: 'Asesoría Legal' },
  { name: 'Atención al Cliente' },
  { name: 'Seguimiento de Trámite' },
];

const usefulInfo = [
  { name: 'Guía de Trámites' },
  { name: 'Preguntas Frecuentes' },
  { name: 'Horarios de Atención' },
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
      {institutions.map((institution, index) => (
        <li key={index}>{institution.name}</li>
      ))}
    </ul>
    <h3>Servicios Adicionales</h3>
    <ul>
      {additionalServices.map((service, index) => (
        <li key={index}>{service.name}</li>
      ))}
    </ul>
    <h3>Información Útil</h3>
    <ul>
      {usefulInfo.map((info, index) => (
        <li key={index}>{info.name}</li>
      ))}
    </ul>
  </div>
);

export default ChatSidebar;
