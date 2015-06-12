"use strict";

import React from 'react';
import {RouteHandler} from 'react-router';
import {Map} from 'immutable';
import * as actions from '../../actions/users';
import * as store from '../../stores/users';
import {flash} from '../../actions/flashMessages';
import Component from '../../lib/component';
import Spinner from './../components/spinner';
import Wrapper from './../components/wrapper';
import Header from './app/components/header';

class App extends Component {

  componentDidMount() {
    // ask for currently logged in user
    actions.getLoggedIn().catch((err) => {
      flash(err.message, 'danger');

      if (err.status === 401) {
        this.redirectWhenUnauthorized();
      }
    });
  }

  redirectWhenUnauthorized() {
    this.props.router.replaceWith('sign-in');
  }

  render() {
    const user = store.getLoggedIn();

    if (actions.getLoggedIn.pending || !user) {
      return <Spinner fullscreen={true} />;
    }

    return (
      <Wrapper>
        <Header user={user} {...this.props} />
        <RouteHandler {...this.props} />
      </Wrapper>
    )
  }

}

App.propTypes = {
  router: React.PropTypes.func,
  pendingActions: React.PropTypes.instanceOf(Map).isRequired
};

export default App;
