import React from 'react';
import { render } from 'react-dom';
import { HelloWorld } from './components/HelloWorld';
import { App1Container } from './containers/App1Container';
// Uncomment Below when Ready to include redux
// import { allReducers } from './reducers';
// import { createStore } from 'redux';
// import { Provider } from 'react-redux';

render(<App1Container />, document.getElementById('react-root'))
