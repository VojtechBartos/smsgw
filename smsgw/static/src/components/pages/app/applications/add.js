"use strict";

import React from 'react';
import {List} from 'immutable';
import {flash} from '../../../../actions/flashMessages';
import {create} from '../../../../actions/applications';
import Component from '../../../../lib/component';
import Subheader from '../components/sub-header';
import FlashMessages from '../../../components/flash-messages';
import Form from './form';

class Add extends Component {

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.applicationForm;
    if (form.isValid()) {
      create(form.getData()).then(() => {
        this.redirectOnSuccess();
      });
    }
  }

  redirectOnSuccess() {
    this.props.router.replaceWith('applications');
  }

  render() {
    const messages = this.props.flashMessages;

    return (
      <div>
        <Subheader backTitle="Applications"
                   backRoute="applications"
                   router={this.props.router}>
          <h1>Add application</h1>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form onSubmit={e => this.onFormSubmit(e)}
                ref="applicationForm"
                pending={create.pending} />
        </div>
      </div>
    );
  }

}

Add.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(List).isRequired
};

export default Add;