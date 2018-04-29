import React, { Component } from 'react';
import './Login.css';

class Login extends Component {
  render() {
    return (
       <div className="container">
  <div className="form-container flip">
    <form className="login-form">
      <h3 className="title">WordCounter Deluxe</h3>
      <div className="form-group" id="username">
        <input className="form-input" tooltip-className="username-tooltip" placeholder="Username" id="email" required="true"></input>
        <span id="username-tool"className="tooltip username-tooltip">What's your username?</span>
      </div>
      <div className="form-group" id="password">
        <input type="password" className="form-input" tooltip-className="password-tooltip" placeholder="Password"></input>
        <span className="tooltip password-tooltip">What's your password?</span>
      </div>
      <div className="form-group">
        <button className="login-button">Login</button>
        <input className="remember-checkbox"type="checkbox"></input>
        <p className="remember-p">Remember me</p>
      </div>
    </form>
    <div className='loader loader2'>
  <div>
    <div>
      <div>
        <div>
          <div>
            <div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
  </div>
</div>
    );
  }
}

export default Login;
