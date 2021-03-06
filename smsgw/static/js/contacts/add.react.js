'use strict';

import React from 'react';
import Immutable from 'immutable';
import {create} from './actions';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';
import Form from './form.react';

class Add extends Component {

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.contactForm;
    if (form.isValid())
      create(form.getData()).then(() => {
        this.redirectOnSuccess();
      });
  }

  redirectOnSuccess() {
    this.props.router.transitionTo('contacts');
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div>
        <Subheader backTitle="Contacts" router={this.props.router}>
          <h1>Add contact</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={(e) => this.onFormSubmit(e)}
                ref="contactForm"
                pending={create.pending}
                {...this.props} />
        </div>
      </div>
    );
  }

}

Add.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default Add;
