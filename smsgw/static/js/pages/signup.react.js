"use strict";

import React from 'react';
import {Link} from 'react-router';
import Immutable from 'immutable';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import SignUpForm from '../users/signup.react';

class SignUp extends Component {

  componentWillReceiveProps(nextProps) {
    // TODO(vojta) if user is already signed in, redirect him to dashboard
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div id="sign">
        <h1><strong>sms</strong>gw</h1>
        <h2>sign up</h2>

        <div className="cleaner"></div>

        <FlashMessages messages={messages} />

        <SignUpForm {...this.props} />

        <div className="info">
          Have an account already? <Link to="signin">Sign in</Link>.
        </div>
      </div>
    );
  }

}

SignUp.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default SignUp;
