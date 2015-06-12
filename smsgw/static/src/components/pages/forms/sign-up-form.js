"use strict";

import React from 'react';
import LaddaButton from 'react-ladda';

class SignUpForm extends React.Component {

  isValid() {
    return true;
  }

  getData() {
    return {
      email: this.refs.email.getDOMNode().value,
      password: this.refs.password.getDOMNode().value,
      firstName: this.refs.firstName.getDOMNode().value,
      lastName: this.refs.lastName.getDOMNode().value,
      company: this.refs.company.getDOMNode().value
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
        <div className="form-group">
            <input type="text"
                   name="firstName"
                   ref="firstName"
                   className="form-control"
                   placeholder="First name"
                   disabled={this.props.pending}
                   required />
        </div>
        <div className="form-group">
          <input type="text"
                 name="lastName"
                 ref="lastName"
                 className="form-control"
                 placeholder="Last name"
                 disabled={this.props.pending}
                 required />
        </div>
        <div className="form-group">
          <input type="text"
                 name="company"
                 ref="company"
                 className="form-control"
                 disabled={this.props.pending}
                 placeholder="Company" />
        </div>
        <LaddaButton
            active={this.props.pending}
            style="expand-right">
            <button>Sign up</button>
        </LaddaButton>
      </form>
    );
  }

}

SignUpForm.propTypes = {
  onSubmit: React.PropTypes.func.isRequired,
  pending: React.PropTypes.bool
};

export default SignUpForm;
