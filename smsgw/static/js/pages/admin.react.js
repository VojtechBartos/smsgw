'use strict';

import React from 'react';
import {getLoggedIn} from '../users/store';
import Component from '../components/component.react';
import Wrapper from '../components/wrapper.react';

class Admin extends Component {

  componentDidMount() {
    const user = getLoggedIn();
    if (user && user.role !== 'admin')
      this.redirectToDashboard();
  }

  redirectToDashboard() {
    this.props.router.transitionTo('dashboard');
  }

  render() {
    return <Wrapper {...this.props} />;
  }

}

Admin.propTypes = {
  router: React.PropTypes.func
};

export default Admin;
