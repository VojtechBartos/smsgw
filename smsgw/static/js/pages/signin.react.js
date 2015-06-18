"use strict";

import React from 'react';
import {Link} from 'react-router';
import Immutable from 'immutable';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import SignInForm from '../users/signin.react';

class SignIn extends Component {

  componentWillReceiveProps(nextProps) {
    // TODO(vojta) if user is already signed in, redirect him to dashboard
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div id="sign">
        <h1><strong>sms</strong>gw</h1>
        <h2>sign in</h2>

        <div className="cleaner"></div>

        <FlashMessages messages={messages} />

        <SignInForm {...this.props} />

        <div className="info">
          Forgot your password? Reset Password.<br />
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
