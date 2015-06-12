"use strict";

import React from 'react';
import {Link} from 'react-router';
import Immutable from 'immutable';
import {signIn, setToken} from '../../actions/users';
import {getLoggedIn} from '../../stores/users';
import Component from '../../lib/component';
import FlashMessages from '../components/flash-messages';
import SignInForm from './forms/sign-in-form';

class SignIn extends Component {

  componentWillReceiveProps(nextProps) {
    // TODO(vojta) if user is already signed in, redirect him to dashboard
  }

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.signInForm;
    if (form.isValid()) {
      signIn(form.getData()).then(() => {
        this.redirectAfterLogin();
      });
    }
  }

  redirectAfterLogin() {
    this.props.router.replaceWith('dashboard');
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div id="sign">
        <h1><strong>sms</strong>gw</h1>
        <h2>sign in</h2>

        <div className="cleaner"></div>

        <FlashMessages messages={messages} />

        <SignInForm
            ref="signInForm"
            onSubmit={(e) => this.onFormSubmit(e)}
            pending={signIn.pending} />

        <div className="info">
          Forgot your password? <Link to="reset-password">Reset Password</Link>.<br />
          Don't have an account? <Link to="sign-up">Sign up</Link> for free.
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
