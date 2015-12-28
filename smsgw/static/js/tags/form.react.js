'use strict';

import React from 'react';
import {findDOMNode} from 'react-dom';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col} from 'react-bootstrap';
import Component from '../components/component.react';

class Form extends Component {

  isValid() {
    return true;
  }

  getData() {
    return {
      label: findDOMNode(this.refs.label).value,
      note: findDOMNode(this.refs.note).value
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
                <label>Note</label>
                <textarea name="note"
                          ref="note"
                          disabled={this.props.pending}
                          defaultValue={this.props.data.note}
                          className="form-control"
                          rows={10}></textarea>
              </div>

              <div className="cleaner" />

              <LaddaButton loading={this.props.pending}
                           buttonStyle="slide-right">
                {this.props.submitTitle}
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
