import React, { Component } from 'react';
import { instanceOf } from 'prop-types';
import { withCookies, Cookies } from 'react-cookie';
import WordCounter from "./WordCounter";
import ReCAPTCHA from "react-google-recaptcha";
import './Login.css';


export const loadingCss = (
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
);
class Login extends Component {
  static propTypes = {
    cookies: instanceOf(Cookies).isRequired
  };

  constructor(){
    super();
    this.state = {
      loading: false,
      authenticated: false,
      captcha: false,
      username: null,
      password: null
    }
  }

  loginCredentials(){
    this.setState({loading: true});
    console.log(this.state.captcha);
  }

  checkUserLoggedIn(){
    const { cookies } = this.props;
    let user = cookies.get('user') ;
    console.log(user);
    //TODO delete me for debugging
    return user !== undefined;
    // return true;
  }
    componentWillMount(){
    if (this.checkUserLoggedIn()){
      this.setState({authenticated: true})
    }
  }
  onCaptchaChange(value) {
  console.log('changed'+value);
  this.setState({captcha: true});
  }
  handleChange = name => event => {
    this.setState({
      [name]: event.target.value,
    });
  };

  render() {
    const loginForm = (
        <div className="login-form">
      <h3 className="title">WordCounter Deluxe</h3>
      <div className="form-group" id="username">
        <input className="form-input" onChange={this.handleChange('username')} placeholder="Username" name="username" required="true"></input>
      </div>
      <div className="form-group" id="password">
        <input name="password" onChange={this.handleChange('password')} type="password" className="form-input" placeholder="Password"></input>
      </div>
      <div className="form-group">
        <ReCAPTCHA
        ref="recaptcha"
        sitekey="6LclY1YUAAAAAEyL_gQtYRkZ_FMS_jqfNDsnKGUA"
        onChange={this.onCaptchaChange.bind(this)}
       />
      </div>
         <div className="form-group">
            <button onClick={this.loginCredentials.bind(this)}
              className="login-button">Login</button>
          </div>
        </div>
    );
    let display = this.state.loading? loadingCss : loginForm;
    display = this.state.authenticated? (<WordCounter/>) : display;
    return (
       <div className="container">
        <div className="form-container flip">
            {display}
        </div>
      </div>
    );
  }
}

export default withCookies(Login);
