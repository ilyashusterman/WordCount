import React, { Component } from 'react';
import './App.css';
import Login from "./Login";
import { CookiesProvider } from 'react-cookie';

class App extends Component {
  render() {
    return (
         <CookiesProvider>
        <Login />
         </CookiesProvider>
    );
  }
}

export default App;
