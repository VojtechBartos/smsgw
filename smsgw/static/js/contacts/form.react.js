"use strict";

import React from 'react';
import LaddaButton from 'react-ladda'
import {Grid, Row, Col, Label} from 'react-bootstrap';
import Component from '../components/component.react';
import AutocompleteInput from '../components/autocompleteinput.react';

class Form extends Component {

  constructor(props) {
    super(props);
    this.state = {
      selected: this.props.tags || [],
      search: []
    };
  }

  isValid() {
    return true;
  }

  getData() {
    return {
      firstName: this.firstName.getDOMNode().value,
      lastName: this.lastName.getDOMNode().value,
      phoneNumber: this.phoneNumber.getDOMNode().value,
      email: this.email.getDOMNode().value,
      note: this.note.getDOMNode().value
    };
  }

  onChange(value) {
    // TODO(vojta)
  }

  onSelect(tag) {
    // TODO(vojta)
  }

  onDelete(index) {
    // TODO(vojta)
  }

  render() {
    return (
      <form onSubmit={e => this.props.onSubmit(e)}>
        <Grid fluid={true}>
          <Row>
            <Col md={3}>
              <div className="form-group">
                <label>First name</label>
                <input type="text"
                       name="firstName"
                       ref="firstName"
                       className="form-control"
                       placeholder="First name"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.firstName}
                       required />
              </div>
              <div className="form-group">
                <label>Last name</label>
                <input type="text"
                       name="lastName"
                       ref="lastName"
                       className="form-control"
                       placeholder="Last name"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.lastName}
                       required />
              </div>
              <div className="form-group">
                <label>Phone number</label>
                <input type="text"
                       name="phoneNumber"
                       ref="phoneNumber"
                       className="form-control"
                       placeholder="Phone number"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.phoneNumber}
                       required />
              </div>
              <div className="form-group">
                <label>Email</label>
                <input type="email"
                       name="email"
                       ref="email"
                       className="form-control"
                       placeholder="Email"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.email} />
              </div>
            </Col>
            <Col md={3}>
                <div className="form-group">
                  <label>Note</label>
                  <textarea name="note"
                            ref="note"
                            rows={5}
                            className="form-control"
                            disabled={this.props.pending}
                            defaultValue={this.props.data.note}>
                  </textarea>
                </div>
            </Col>
            <Col md={2}>
              <div className="form-group">
                <label>Tags</label>
                <AutocompleteInput pending={false}
                                   onChange={this.onChange}
                                   onSelect={this.onSelect}
                                   options={this.state.search} />
                <div className="cleaner" />
                <ul>{tags}</ul>
              </div>
            </Col>
          </Row>
          <Row>
            <Col md={3}>
              <LaddaButton active={this.props.pending}
                           style="expand-right">
                <button>{this.props.submitTitle}</button>
              </LaddaButton>
            </Col>
          </Row>
        </Grid>
      </form>
    );
  }

}

export default Form;