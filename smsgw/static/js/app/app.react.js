'use strict';

import React from 'react';
import {RouteHandler} from 'react-router';
import {Map} from 'immutable';
import * as actions from '../users/actions';
import * as store from '../users/store';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';
import Wrapper from '../components/wrapper.react';
import Header from './header.react';

class App extends Component {

  componentDidMount() {
    // ask for currently logged in user
    actions.getLoggedIn().catch((err) => {
      flash(err.message, 'danger');

      if (err.status === 401)
        this.redirectWhenUnauthorized();
    });
  }

  redirectWhenUnauthorized() {
    this.props.router.transitionTo('signin');
  }

  render() {
    const user = store.getLoggedIn();

    if (actions.getLoggedIn.pending || !user)
      return <Spinner fullscreen={true} />;

    return (
      <Wrapper>
        <Header user={user} {...this.props} />
        <RouteHandler {...this.props} />
      </Wrapper>
    );
  }

}

App.propTypes = {
  router: React.PropTypes.func,
  pendingActions: React.PropTypes.instanceOf(Map).isRequired
};

export default App;
