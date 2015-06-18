"use string";

import React from 'react';
import {List} from 'immutable';
import {getLoggedIn} from '../users/store';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';
import SettingsForm from '../users/settings.react';

class Settings extends Component {

  render() {
    const user = getLoggedIn();
    const messages = this.props.flashMessages;

    return (
      <div>
        <Subheader router={this.props.router}>
          <h1>Settings</h1>
          <h2>{user.firstName} {user.lastName}</h2>
        </Subheader>

        <div id="context">
          <FlashMessages messages={messages} />

          <SettingsForm user={user} {...this.props} />
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
