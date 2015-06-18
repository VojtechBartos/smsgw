"use strict";

import React from 'react';
import Component from '../components/component.react';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col} from 'react-bootstrap';

class Form extends Component {

  isValid() {
    return true;
  }

  getData() {
    return {
      label: this.refs.label.getDOMNode().value,
      prefix: this.refs.prefix.getDOMNode().value,
      callbackUrl: this.refs.callbackUrl.getDOMNode().value,
      note: this.refs.note.getDOMNode().value
    };
  }

  render() {
    return (
      <form onSubmit={this.props.onSubmit}>
        <Grid fluid={true}>
          <Row>
            <Col md={4}>
              <div className="form-group">
                <label>Label</label>
                <input type="text"
                       name="label"
                       ref="label"
                       placeholder="Label"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.label}
                       className="form-control"
                       required />
              </div>
              <div className="form-group">
                <label>Prefix</label>
                <input type="text"
                       name="prefix"
                       ref="prefix"
                       placeholder="Prefix"
                       className="form-control"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.prefix} />
              </div>
              <div className="form-group">
                <label>Callback url</label>
                <input type="url"
                       name="callbackUrl"
                       ref="callbackUrl"
                       placeholder="Callback url"
                       className="form-control"
                       disabled={this.props.pending}
                       defaultValue={this.props.data.callbackUrl} />
              </div>
              <div className="form-group">
                <label>Note</label>
                <textarea name="note"
                          ref="note"
                          disabled={this.props.pending}
                          defaultValue={this.props.data.note}
                          className="form-control"
                          rows={10}></textarea>
              </div>

              <div className="cleaner" />

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

Form.defaultProps = {
  pending: false,
  submitTitle: 'Create',
  data: {}
};

export default Form;