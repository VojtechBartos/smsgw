"use strict";

import React from 'react';
import LaddaButton from 'react-ladda';

class SignInForm extends React.Component {

  isValid() {
    return true;
  }

  getData() {
    return {
      email: this.refs.email.getDOMNode().value,
      password: this.refs.password.getDOMNode().value
    };
  }

  render() {
    return (
      <form onSubmit={this.props.onSubmit}>
        <div className="form-group">
            <input type="email"
                   name="email"
                   ref="email"
                   className="form-control"
                   placeholder="E-mail"
                   disabled={this.props.pending}
                   required />
        </div>
        <div className="form-group">
            <input type="password"
                   name="password"
                   ref="password"
                   className="form-control"
                   placeholder="Password"
                   disabled={this.props.pending}
                   required />
        </div>
        <LaddaButton
            active={this.props.pending}
            style="expand-right">
            <button>Sign in</button>
        </LaddaButton>
      </form>
    );
  }

}

SignInForm.propTypes = {
  onSubmit: React.PropTypes.func.isRequired,
  pending: React.PropTypes.bool
};

export default SignInForm;
