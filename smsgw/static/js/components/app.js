'use strict';

import React from 'react';
import {RouteHandler} from 'react-router';
import * as appState from '../state';
import Component from '../lib/component';
import Wrapper from './components/wrapper';

// import stores
import '../stores/users';
import '../stores/templates';
import '../stores/flashMessages';
import '../stores/contacts';
import '../stores/tags';
import '../stores/outbox';
import '../stores/applications';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = this.getState();
  }

  getState() {
    return {
      pendingActions: appState.pendingActionsCursor(),
      flashMessages: appState.flashMessagesCursor(),
      users: appState.usersCursor(),
      templates: appState.templatesCursor(),
      contacts: appState.contactsCursor(),
      tags: appState.tagsCursor(),
      outbox: appState.outboxCursor(),
      applications: appState.applicationsCursor()
    };
  }

  componentDidMount() {
    // event listener on app state change
    appState.state.on('change', () => {
      console.time('app render');
      this.setState(this.getState(), () => {
        console.timeEnd('app render');
      });
    });
  }

  render() {
    return <RouteHandler {...this.state} router={this.context.router} />
  }

}

export default App;
