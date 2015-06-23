'use strict';

import React from 'react';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col} from 'react-bootstrap';
import Component from '../components/component.react';
import {update} from './actions';
import {flash} from '../flashMessages/actions';

class Settings extends Component {

  isValid() {
    let isValid = true;
    let password = this.refs.password.getDOMNode().value;
    let passwordVerify = this.refs.password.getDOMNode().value;

    if (password || password.length > 0)
      if (password !== passwordVerify) {
        isValid = false;

        flash('Password and verify password needs to be same.');
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

  onFormSubmit(e) {
    e.preventDefault();

    if (this.isValid())
      update('@me', this.getData()).then(() => {
        flash('Successfully saved.');
      });
  }

  render() {
    const pending = update.pending;
    const user = this.props.user;

    return (
      <form onSubmit={(e) => this.onFormSubmit(e)}>
        <Grid fluid={true}>
          <Row>
            <Col md={4}>
              <div className="form-group">
                <label>E-Mail</label>
                <input type="email"
                       name="email"
                       ref="email"
                       placeholder="E-mail"
                       disabled={pending}
                       defaultValue={user.email}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>First name</label>
                <input type="text"
                       name="firstName"
                       ref="firstName"
                       placeholder="First name"
                       disabled={pending}
                       defaultValue={user.firstName}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>Last name</label>
                <input type="text"
                       name="lastName"
                       ref="lastName"
                       placeholder="Last name"
                       disabled={pending}
                       defaultValue={user.lastName}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>Company</label>
                <input type="text"
                       name="company"
                       ref="company"
                       placeholder="Comapny"
                       disabled={pending}
                       defaultValue={user.company}
                       className="form-control" />
              </div>

              <div className="form-group">
                <label>Password</label>
                <input type="password"
                       name="password"
                       ref="password"
                       placeholder="Password"
                       disabled={pending}
                       className="form-control" />
              </div>
              <div className="form-group">
                <label>Verify password</label>
                <input type="password"
                       name="passwordVerify"
                       ref="passwordVerify"
                       placeholder="Verify password"
                       disabled={pending}
                       className="form-control" />
              </div>

              <div className="cleaner" />

              <LaddaButton active={pending}
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

Settings.defaultProps = {
  user: {}
};

export default Settings;
