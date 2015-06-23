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
    const form = this.refs.tagForm;
    if (form.isValid())
      create(form.getData()).then(() => {
        this.redirectOnSuccess();
      });
  }

  redirectOnSuccess() {
    this.props.router.replaceWith('tags');
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div>
        <Subheader backTitle="Tags" router={this.props.router}>
          <h1>Add tag</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={(e) => this.onFormSubmit(e)}
                ref="tagForm"
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
