"use strict";

import React from 'react';
import LaddaButton from 'react-ladda';
import {signUp} from './actions';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';

class SignUp extends Component {

  getData() {
    return {
      email: this.refs.email.getDOMNode().value,
      password: this.refs.password.getDOMNode().value,
      firstName: this.refs.firstName.getDOMNode().value,
      lastName: this.refs.lastName.getDOMNode().value,
      company: this.refs.company.getDOMNode().value
    };
  }

  onFormSubmit(e) {
    e.preventDefault();

    signUp(this.getData()).then(() => {
      this.redirectAfterSignUp();
    });
  }

  redirectAfterSignUp() {
    this.props.router.transitionTo('signin');

    flash("Signed up. Now you can login.");
  }

  render() {
    const pending = signUp.pending;

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
        <LaddaButton
            active={pending}
            style="expand-right">
            <button>Sign up</button>
        </LaddaButton>
      </form>
    );
  }

}

SignUp.propTypes = {
  router: React.PropTypes.func
};

export default SignUp;
