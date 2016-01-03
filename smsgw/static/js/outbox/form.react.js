'use strict';

import React from 'react';
import {findDOMNode} from 'react-dom';
import moment from 'moment';
import {Map} from 'immutable';
import LaddaButton from 'react-ladda';
import {Grid, Row, Col, Input} from 'react-bootstrap';
import DateTimeField from 'react-bootstrap-datetimepicker';
import ReactTagsInput from 'react-tagsinput';
import Component from '../components/component.react';
import {search as tagsActionSearch} from '../tags/actions';
import {validate} from './actions';
import Tag from '../tags/tag';
import {search as contactsActionSearch} from '../contacts/actions';
import Contact from '../contacts/contact';


class Form extends Component {

  constructor(props) {
    super(props);
    this.state = {
      message: '',
      send: moment(),
      completions: []
    };
  }

  isValid() {
    return true;
  }

  getData() {
    const items = this.refs.respondents.getTags().map(el => el.props.tag);
    return {
      send: this.state.send.utc().format('YYYY-MM-DD HH:mm:ss'),
      message: findDOMNode(this.refs.text).value,
      tags: items.filter(i => i instanceof Tag),
      contacts: items.filter(i => i instanceof Contact),
      phoneNumbers: items.filter(i => typeof i === 'string' || i instanceof String)
    };
  }

  // Events

  onChangeTemplate(e) {
    const template = this.props.templates.get(e.target.value);

    if (template)
      this.setState({ message: template.text });
  }

  onChangeMessage(e) {
    this.setState({
      message: e.target.value
    });
  }

  onChangeDateTime(timestamp) {
    this.setState({ send: moment(timestamp, 'x') });
  }

  // React Tags Input

  beforeTagAdd(item) {
    if (item instanceof Contact || item instanceof Tag)
      return true;

    if (this.state.completions.size > 0)
      return false;

    return true;
  }

  addTag(item) {
    this.refs.respondents.addTag(item);

    this.setState({ completions: Map() });
  }

  validateAsync(item, cb) {
    // TODO(vojta) add validation
    const tag = item.props.tag;
    if (typeof tag === 'string' || tag instanceof String)
      return validate(tag).then(() => cb(true))
                          .error(() => cb(false));

    cb(true);
  }

  complete(value) {
    if (!value || value === '') {
      this.setState({ completions: Map() });
      return;
    }

    contactsActionSearch(value)
      .then(() => {
        return tagsActionSearch(value);
      })
      .then(() => {
        const { contactsSearch, tagsSearch } = this.props;

        this.setState({
          completions: contactsSearch.merge(tagsSearch)
        });
      });
  }

  transform(item) {
    // TODO(vojta) find better way of passing items, also create separate
    // component
    let label = item;
    if (item instanceof Contact)
      label = `${item.firstName} ${item.lastName}`;

    if (item instanceof Tag)
      label = `${item.label}`;

    return <span tag={item}>{label}</span>;
  }

  renderTag(key, element, removeTag) {
    const tag = element.props.tag;
    const className = [
      'react-tagsinput-tag',
      (tag instanceof Contact) ? 'contact' : null
    ];

    return (
      <span key={key} className={className.join(' ')}>
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
    const templates = this.props.templates;
    const dateTimeOptions = { ref: 'send', required: true, disabled: true };
    const { send } = this.state;

    return (
      <form onSubmit={this.props.onSubmit}>
        <Grid fluid={true}>
          <Row>
            <Col md={4}>
              <div className="form-group">
                <label>To who:</label>
                <ReactTagsInput ref="respondents"
                                placeholder="Add contact"
                                addOnBlur={false}
                                validateAsync={(tag, cb) => this.validateAsync(tag, cb)}
                                beforeTagAdd={tag => this.beforeTagAdd(tag)}
                                transform={tag => this.transform(tag)}
                                renderTag={(...props) => this.renderTag(...props)}
                                onChangeInput={tag => this.complete(tag)} />
                <div className="react-tagsinput-completion">
                  {this.state.completions.map((item, index) => {
                    return React.cloneElement(
                      this.renderTag(index, this.transform(item)),
                      { onClick: () => this.addTag(item) }
                    );
                  })}
                </div>
              </div>

              <div className="cleaner" />

              <Input type='select'
                     label='Use template'
                     onChange={(e) => this.onChangeTemplate(e)} >
                <option>Choose template</option>
                  {templates.toArray().map((template, index) => {
                    return (
                      <option key={index} value={template.uuid}>
                        {template.label}
                      </option>
                    );
                  })}
              </Input>

              <div className="form-group">
                <label>Message ({this.state.message.length}/160)</label>
                <textarea name="text"
                          ref="text"
                          disabled={this.props.pending}
                          className="form-control"
                          value={this.state.message}
                          onChange={(e) => this.onChangeMessage(e)}
                          required
                          rows={10}></textarea>
              </div>
            </Col>
            <Col md={3}>
              <div className="form-group">
                <label>Send at</label>

                <DateTimeField dateTime={send.format('x')}
                               onChange={value => this.onChangeDateTime(value)}
                               minDate={moment()}
                               inputFormat="HH:mm DD/MM/YYYY"
                               inputProps={dateTimeOptions}/>
              </div>
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
  templates: Map()
};

Form.propTypes = {
  templates: React.PropTypes.instanceOf(Map).isRequired,
  contactsSearch: React.PropTypes.instanceOf(Map).isRequired,
  tagsSearch: React.PropTypes.instanceOf(Map).isRequired
};

export default Form;
