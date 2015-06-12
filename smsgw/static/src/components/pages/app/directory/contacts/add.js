"use strict";

import React from 'react';
import Immutable from 'immutable';
import {create} from '../../../../../actions/contacts';
import Component from '../../../../../lib/component';
import FlashMessages from '../../../../components/flash-messages';
import Subheader from '../../components/sub-header';
import Form from './form.coffee';

class Add extends Component {

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.contactForm;
    if (form.isValid()) {
      create(form.getData()).then(() => {
        this.redirectOnSuccess();
      });
    }
  }

  redirectOnSuccess() {
    this.props.router.replaceWith('contacts');
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
                pending={create.pending} />
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
