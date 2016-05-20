'use strict';

import React from 'react';
import LaddaButton from 'react-ladda';
import ReactTagsInput from 'react-tagsinput';
import {Grid, Row, Col} from 'react-bootstrap';
import {Map} from 'immutable';
import Component from '../components/component.react';
import Tag from '../tags/tag';
import {search as tagsActionSearch} from '../tags/actions';


class Form extends Component {

  constructor(props) {
    super(props);
    this.state = {
      selected: this.props.tags,
      completions: Map()
    };
  }

  isValid() {
    return true;
  }

  getData() {
    return {
      firstName: this.refs.firstName.getDOMNode().value,
      lastName: this.refs.lastName.getDOMNode().value,
      phoneNumber: this.refs.phoneNumber.getDOMNode().value,
      email: this.refs.email.getDOMNode().value,
      note: this.refs.note.getDOMNode().value,
      tags: this.refs.tags.getTags().map(el => {
        const tag = el.props.tag;
        return (tag instanceof Tag) ? tag.label : tag;
      })
    };
  }

  // React Tags Input

  addTag(item) {
    this.refs.tags.addTag(item);

    this.setState({ completions: Map() });
  }

  validate(item) {
    const tag = item.props.tag;
    if (typeof tag === 'string' || tag instanceof String)
      return tag.trim().length > 0;

    return true;
  }

  complete(value) {
    if (!value || value === '') {
      this.setState({ completions: Map() });
      return;
    }

    tagsActionSearch(value).then(() => {
      const { tagsSearch } = this.props;

      this.setState({ completions: tagsSearch });
    });
  }

  transform(item) {
    return (
      <span tag={item}>
        {(item instanceof Tag) ? item.label : item}
      </span>
    );
  }

  renderTag(key, element, removeTag) {
    return (
      <span key={key} className="react-tagsinput-tag">
        {element}
        {(() => {
          if (!removeTag) return null;
          return <a onClick={removeTag} className="react-tagsinput-remove" />;
        })()}
      </span>
    );
  }

  // Render

  render() {
    let tags = [];
    if (this.props.data.tags)
      tags = this.props.data.tags.map(item => this.transform(item));

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
                  <ReactTagsInput ref="tags"
                                  placeholder="Add tag"
                                  addOnBlur={true}
                                  defaultValue={tags}
                                  validate={tag => this.validate(tag)}
                                  transform={tag => this.transform(tag)}
                                  renderTag={(...props) => this.renderTag(...props)}
                                  onChangeInput={tag => this.complete(tag)} />
                  <div className="react-tagsinput-completion">
                    {this.state.completions.toArray().map((item, index) => {
                      return React.cloneElement(
                        this.renderTag(index, this.transform(item)),
                        { onClick: () => this.addTag(item) }
                      );
                    })}
                  </div>
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

Form.defaultProps = {
  pending: false,
  submitTitle: 'Create',
  data: {},
  tags: []
};

Form.propTypes = {
  tagsSearch: React.PropTypes.instanceOf(Map).isRequired
};

export default Form;
