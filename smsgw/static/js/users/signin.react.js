'use strict';

import React from 'react';
import {Link} from 'react-router';
import LaddaButton from 'react-ladda';
import Immutable from 'immutable';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import {signIn, getToken} from './actions';

class SignIn extends Component {

  componentDidMount() {
    if (getToken())
      this.redirectAfterLogin();
  }

  onFormSubmit(e) {
    e.preventDefault();

    const data = {
      email: this.refs.email.getDOMNode().value,
      password: this.refs.password.getDOMNode().value
    };

    signIn(data).then(() => {
      this.redirectAfterLogin();
    });
  }

  redirectAfterLogin() {
    this.props.router.transitionTo('dashboard');
  }

  render() {
    const messages = this.props.flashMessages;
    const pending = signIn.pending;

    return (
      <div id="sign">
        <h1><strong>sms</strong>gw</h1>
        <h2>sign in</h2>

        <div className="cleaner"></div>

        <FlashMessages messages={messages} />

        <form onSubmit={(e) => this.onFormSubmit(e)}>
          <div className="form-group">
              <input type="email"
                     name="email"
                     ref="email"
                     className="form-control"
                     placeholder="E-mail"
                     disabled={pending}
                     required />
          </div>
          <div className="form-group">
              <input type="password"
                     name="password"
                     ref="password"
                     className="form-control"
                     placeholder="Password"
                     disabled={pending}
                     required />
          </div>
          <LaddaButton
              active={pending}
              style="expand-right">
              <button>Sign in</button>
          </LaddaButton>
        </form>

        <div className="info">
          Don't have an account? <Link to="signup">Sign up</Link> for free.
        </div>
      </div>
    );
  }

}

SignIn.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default SignIn;
