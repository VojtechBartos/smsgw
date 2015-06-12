"use string";

import React from 'react';
import {List} from 'immutable';
import {getLoggedIn} from '../../../stores/users';
import {update} from '../../../actions/users';
import {flash} from '../../../actions/flashMessages';
import Component from '../../../lib/component';
import FlashMessages from '../../components/flash-messages';
import Form from './forms/settings-form';
import Subheader from './components/sub-header';


class Settings extends Component {

  onFormSubbmit(e) {
    e.preventDefault();
    const form = this.refs.settingsForm;
    if (form.isValid()) {
      update('@me', form.getData()).then(() => {
        flash('Successfully saved.');
      });
    }
  }

  onFormError(err) {
    flash(err.message, 'danger');
  }

  render() {
    const user = getLoggedIn();
    const messages = this.props.flashMessages;
    const pending = update.pending;

    return (
      <div>
        <Subheader router={this.props.router}>
          <h1>Settings</h1>
          <h2>{user.firstName} {user.lastName}</h2>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <Form
              onSubmit={(e) => this.onFormSubbmit(e)}
              onError={this.onFormError}
              ref="settingsForm"
              pending={pending}
              disabled={pending}
              data={user} />
        </div>
      </div>
    );
  }

}

Settings.propTypes = {
  router: React.PropTypes.func,
  flashMessages: React.PropTypes.instanceOf(List).isRequired
};

export default Settings;
