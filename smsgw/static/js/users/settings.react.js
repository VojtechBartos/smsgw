'use strict';

import React from 'react';
import {List} from 'immutable';
import {getLoggedIn} from './store';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Subheader from '../components/subheader.react';
import Form from './form.react';

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

          <Form user={user} adminVersion={false} {...this.props} />
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
