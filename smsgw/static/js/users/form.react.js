'use strict';

import React from 'react';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col, Input, Table} from 'react-bootstrap';
import Component from '../components/component.react';
import {update} from './actions';
import User from './user';
import {flash} from '../flashMessages/actions';

class Form extends Component {

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
    const { adminVersion } = this.props;
    const password = this.refs.password.getDOMNode().value;
    let data = {
      firstName: this.refs.firstName.getDOMNode().value,
      lastName: this.refs.lastName.getDOMNode().value,
      email: this.refs.email.getDOMNode().value,
      company: this.refs.company.getDOMNode().value,
      password: (password.length === 0) ? null : password
    };

    if (adminVersion) {
      data.role = this.refs.role.getInputDOMNode().value;
      data.isActive = this.refs.isActive.getInputDOMNode().value === 'true';
    }

    return data;
  }

  onFormSubmit(e) {
    e.preventDefault();

    const {user} = this.props;

    if (this.isValid())
      update(user.uuid, this.getData()).then(() => {
        flash('Successfully saved.');
      });
  }

  render() {
    const pending = update.pending;
    const { user, adminVersion } = this.props;

    return (
      <form onSubmit={(e) => this.onFormSubmit(e)}>
        <Grid fluid={true}>
          <Row>
            <Col md={2}>
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
            </Col>

            {(() => {
              if (!adminVersion)
                return null;

              return (
                <Col md={2}>
                  <Input type="select" ref="role" label="Role" defaultValue={user.role}>
                    <option value="user">User</option>
                    <option value="admin">Admin</option>
                  </Input>

                  <Input type="select" ref="isActive" label="Active" defaultValue={user.isActive}>
                    <option value={false}>No</option>
                    <option value={true}>Yes</option>
                  </Input>

                  <label>Statistics</label>
                  <Table responsive>
                    <tbody>
                      <tr>
                        <td>Sent messages</td>
                        <td>{user.numbers.sent}</td>
                      </tr>
                      <tr>
                        <td>Received messages</td>
                        <td>{user.numbers.inbox}</td>
                      </tr>
                      <tr>
                        <td>Waiting messages</td>
                        <td>{user.numbers.outbox}</td>
                      </tr>
                      <tr>
                        <td>Applications</td>
                        <td>{user.numbers.applications}</td>
                      </tr>
                      <tr>
                        <td>Contacts</td>
                        <td>{user.numbers.contacts}</td>
                      </tr>
                      <tr>
                        <td>Tags</td>
                        <td>{user.numbers.tags}</td>
                      </tr>
                      <tr>
                        <td>Templates</td>
                        <td>{user.numbers.templates}</td>
                      </tr>
                    </tbody>
                  </Table>
                </Col>
              );
            })()}
          </Row>
          <Row>
            <Col>
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

Form.defaultProps = {
  user: {},
  adminVersion: false
};

Form.propTypes = {
  user: React.PropTypes.instanceOf(User).isRequired,
  adminVersion: React.PropTypes.bool
};

export default Form;
