import ReactDom from 'react-dom';
import React from 'react';
import App from './app.jsx';


document.addEventListener('DOMContentLoaded', () => {
  ReactDom.render(<App />, document.getElementById('root'));
});
