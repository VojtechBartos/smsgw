'use strict';

import React from 'react';
import {RouteHandler} from 'react-router';
import * as appState from '../state';
import Component from '../components/component.react';

// import stores
import '../users/store';
import '../templates/store';
import '../flashMessages/store';
import '../contacts/store';
import '../tags/store';
import '../outbox/store';
import '../applications/store';

export default class Main extends Component {

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
      console.time('app render'); // eslint-disable-line no-console
      this.setState(this.getState(), () => {
        console.timeEnd('app render'); // eslint-disable-line no-console
      });
    });
  }

  render() {
    return <RouteHandler {...this.state} router={this.context.router} />;
  }

}
