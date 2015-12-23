'use strict';

import React from 'react';
import {findDOMNode} from 'react-dom';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col, Well} from 'react-bootstrap';
import Component from '../components/component.react';

class Form extends Component {

  constructor(props) {
    super(props);
    this.state = {
      length: 0
    };
  }

  isValid() {
    return true;
  }

  getData() {
    return {
      label: findDOMNode(this.refs.label).value,
      text: findDOMNode(this.refs.text).value
    };
  }

  onTextChange(e) {
    this.setState({ length: e.target.value.length });
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
                         className="form-control"
                         placeholder="Label"
                         disabled={this.props.disabled}
                         defaultValue={this.props.data.label}
                         required />
              </div>
              <div className="form-group">
                  <label>Template body ({this.state.length}/160)</label>
                  <textarea name="text"
                            ref="text"
                            rows={10}
                            className="form-control"
                            onChange={(e) => this.onTextChange(e)}
                            disabled={this.props.pending}
                            defaultValue={this.props.data.text}
                            required></textarea>
              </div>
            </Col>
            <Col md={3}>
              <Well bsSize="large" className="margin-top-25">
                You can use some constant wich will be replaced by
                real value. We are
                supporting <strong>{'{firstName} '}</strong>
                 or <strong>{'{lastName} '}</strong> for
                user first name and last name.
              </Well>
            </Col>
          </Row>
          <Row>
            <LaddaButton loading={this.props.pending}
                         buttonStyle="slide-right">
              {this.props.submitTitle}
            </LaddaButton>
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
