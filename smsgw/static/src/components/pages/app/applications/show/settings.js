"use strict";

import React from 'react';
import Immutable from 'immutable';
import {flash} from '../../../../../actions/flashMessages';
import {update} from '../../../../../actions/applications';
import Component from '../../../../../lib/component';
import FlashMessages from '../../../../components/flash-messages';
import Form from '../form';

class Settings extends Component {

  onFormSubmit(e) {
    e.preventDefault();
    const form = this.refs.applicationForm;
    if (form.isValid()) {
      update(this.props.application.uuid, form.getData()).then(() => {
        flash('Successfuly saved.');
      });
    }
  }

  render() {
    const messages = this.props.flashMessages;
    const app = this.props.application;

    return (
      <div id="context">
        <FlashMessages messages={messages} />

        <Form onSubmit={e => this.onFormSubmit(e)}
              ref="applicationForm"
              submitTitle="Save"
              pending={update.pending}
              data={app} />
      </div>
    );
  }

}

Settings.propTypes = {
  application: React.PropTypes.instanceOf(Immutable.Record).isRequired,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default Settings;