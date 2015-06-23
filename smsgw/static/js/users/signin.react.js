'use strict';

import React from 'react';
import LaddaButton from 'react-ladda';
import {signIn} from './actions';
import Component from '../components/component.react';

class SignIn extends Component {

  getData() {
    return {
      email: this.refs.email.getDOMNode().value,
      password: this.refs.password.getDOMNode().value
    };
  }

  onFormSubmit(e) {
    e.preventDefault();

    signIn(this.getData()).then(() => {
      this.redirectAfterLogin();
    });
  }

  redirectAfterLogin() {
    this.props.router.replaceWith('dashboard');
  }

  render() {
    const pending = signIn.pending;

    return (
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
    );
  }

}

SignIn.propTypes = {
  router: React.PropTypes.func
};

export default SignIn;
