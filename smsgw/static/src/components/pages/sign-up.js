"use strict";

import React from 'react';
import {Link} from 'react-router';
import Immutable from 'immutable';
import Component from '../../lib/component';
import {signUp} from '../../actions/users';
import {flash} from '../../actions/flashMessages';
import FlashMessages from '../components/flash-messages';
import SignUpForm from './forms/sign-up-form';

class SignUp extends Component {

  componentWillReceiveProps(nextProps) {
    // TODO(vojta) if user is already signed in, redirect him to dashboard
  }

  onFormSubmit(e) {
    e.preventDefault();
    let form = this.refs.signUpForm;
    if (form.isValid()) {
      signUp(form.getData()).then(() => {
        this.redirectAfterSignUp();
      });
    }
  }

  redirectAfterSignUp() {
    this.props.router.replaceWith('sign-in');

    flash("Signed up. Now you can login.");
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div id="sign">
        <h1><strong>sms</strong>gw</h1>
        <h2>sign up</h2>

        <div className="cleaner"></div>

        <FlashMessages messages={messages} />

        <SignUpForm
          ref="signUpForm"
          onSubmit={(e) => this.onFormSubmit(e)}
          pending={signUp.pending} />

        <div className="info">
          Have an account already? <Link to="sign-in">Sign in</Link>.
        </div>
      </div>
    );
  }

}

SignUp.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired,
  pendingActions: React.PropTypes.instanceOf(Immutable.Map).isRequired
};

export default SignUp;
