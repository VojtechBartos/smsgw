"use strict";

import React from 'react';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col} from 'react-bootstrap';
import Component from '../../../../lib/component';

class Form extends Component {

  isValid() {
    let isValid = true;
    let password = this.refs.password.getDOMNode().value;
    let passwordVerify = this.refs.password.getDOMNode().value;

    if (password || password.length > 0) {
      if (password != passwordVerify) {
        isValid = false;
        const message = "Password and verify password needs to be same.";
        if (this.props.onError) {
          this.props.onError(msg);
        }
      }
    }
    return isValid;
  }

  getData() {
    const password = this.refs.password.getDOMNode().value;

    return {
      firstName: this.refs.firstName.getDOMNode().value,
      lastName: this.refs.lastName.getDOMNode().value,
      email: this.refs.email.getDOMNode().value,
      company: this.refs.company.getDOMNode().value,
      password: (password.length === 0) ? null : password
    };
  }

  render() {
    return (
      <form onSubmit={this.props.onSubmit}>
        <Grid fluid={true}>
          <Row>
            <Col md={4}>
              <div className="form-group">
                <label>E-Mail</label>
                <input type="email"
                       name="email"
                       ref="email"
                       placeholder="E-mail"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.email}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>First name</label>
                <input type="text"
                       name="firstName"
                       ref="firstName"
                       placeholder="First name"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.firstName}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>Last name</label>
                <input type="text"
                       name="lastName"
                       ref="lastName"
                       placeholder="Last name"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.lastName}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>Company</label>
                <input type="text"
                       name="company"
                       ref="company"
                       placeholder="Comapny"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.company}
                       className="form-control" />
              </div>

              <div className="form-group">
                <label>Password</label>
                <input type="password"
                       name="password"
                       ref="password"
                       placeholder="Password"
                       disabled={this.props.pending}
                       className="form-control" />
              </div>
              <div className="form-group">
                <label>Verify password</label>
                <input type="password"
                       name="passwordVerify"
                       ref="passwordVerify"
                       placeholder="Verify password"
                       disabled={this.props.pending}
                       className="form-control" />
              </div>

              <div className="cleaner" />

              <LaddaButton active={this.props.pending}
                           style="expand-right">
                  <button>Save</button>
              </LaddaButton>
            </Col>
          </Row>
        </Grid>
      </form>
    );
  }

}

Form.defaultProps = {
  pending: false,
  data: {}
};

export default Form;