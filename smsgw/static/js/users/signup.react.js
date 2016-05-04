'use strict';

import React from 'react';
import {Link} from 'react-router';
import LaddaButton from 'react-ladda';
import Immutable from 'immutable';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import {signUp, getToken} from './actions';
import {flash} from '../flashMessages/actions';

class SignUp extends Component {

  static willTransitionTo(transition) {
    if (getToken()) transition.redirect('dashboard');
  }

  onFormSubmit(e) {
    e.preventDefault();

    const data = {
      email: this.refs.email.getDOMNode().value,
      password: this.refs.password.getDOMNode().value,
      firstName: this.refs.firstName.getDOMNode().value,
      lastName: this.refs.lastName.getDOMNode().value,
      company: this.refs.company.getDOMNode().value
    };

    signUp(data).then(() => {
      this.redirectAfterSignUp();
    });
  }

  redirecToDashboard() {
    this.props.router.transitionTo('dashboard');
  }

  redirectAfterSignUp() {
    this.props.router.transitionTo('signin');

    flash('Signed up. Now you can login.');
  }

  render() {
    const messages = this.props.flashMessages;
    const pending = signUp.pending;

    return (
      <div id="sign">
        <h1><strong>sms</strong>gw</h1>
        <h2>sign up</h2>

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
          <div className="form-group">
              <input type="text"
                     name="firstName"
                     ref="firstName"
                     className="form-control"
                     placeholder="First name"
                     disabled={pending}
                     required />
          </div>
          <div className="form-group">
            <input type="text"
                   name="lastName"
                   ref="lastName"
                   className="form-control"
                   placeholder="Last name"
                   disabled={pending}
                   required />
          </div>
          <div className="form-group">
            <input type="text"
                   name="company"
                   ref="company"
                   className="form-control"
                   disabled={pending}
                   placeholder="Company" />
          </div>
          <LaddaButton active={pending}
                       style="expand-right">
            <button>Sign up</button>
          </LaddaButton>
        </form>

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
