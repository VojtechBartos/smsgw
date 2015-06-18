"use strict";

import React from 'react';
import Immutable from 'immutable';
import {create} from './actions';
import Form from './form.react';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';

class Add extends React.Component {

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.templateForm;
    if (form.isValid()) {
      create(form.getData()).then(() => {
        this.redirectOnSuccess();
      });
    }
  }

  redirectOnSuccess() {
    this.props.router.transitionTo('templates');
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div>
        <Subheader backTitle="Templates" router={this.props.router}>
          <h1>Add template</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={(e) => this.onFormSubmit(e)}
                ref="templateForm"
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
