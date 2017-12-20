import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import {userActions} from './user.actions';


class LoginPage extends Component{

  constructor(props){
    super(props);
    this.state = {
      email: '',
      password: '',
      isSubmitted: false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e){
    const {email, value} = e.target;
    this.setState({[email]: value});
  }

  handleSubmit(e){
    e.preventDefault();

    this.setState({ submitted: true });
    const { email, password } = this.state;
    const { dispatch } = this.props;
    if (email && password) {
      dispatch(userActions.login(email, password));
    }
  }

  render(){
    const {logginIn} = this.props;
    const {email, password, isSubmitted} = this.state;
    return(
      <div className="App">
        <header className="App-header">
          <h2>Beblue Maya</h2>
        </header>  
        <div id="vertical">
          <div className="App-form-box">
            <form onSubmit={this.handleSubmit}>
              <div>
                <div className="App-login-box">
                  <label for="login-box" id="login-label">email</label>
                  <input id="login-box" type="email" onChange={this.handleChange} />
                  {isSubmitted && !email &&
                    <div className="help-block">email is required</div>
                  }      
                </div>
              </div>
              <div>
                <div className= "App-login-box">
                  <label id="login-label">Senha</label>
                  <input id="login-box" type="password" onChange={this.handleChange}/>
                  {isSubmitted && !password &&
                    <div className="help-block">senha is required</div>
                  }
                  
                </div>
              </div>
              <div>
                <div className="App-button">
                  <button type="submit" id="button">SIGN IN </button>      
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>  
    );
  }

  mapStateToProps(state) {
    const { loggingIn } = state.authentication;
    return {
        loggingIn
    };
  }

  /*setEmailID = (e) => {
    this.setState({
      emailID: e.target.value,
      loginError: ''
    });
  };

  setPassword = (e) => {
    this.setState({
      password: e.target.value,
      loginError: ''
    });
  };
  */
}

export default LoginPage;