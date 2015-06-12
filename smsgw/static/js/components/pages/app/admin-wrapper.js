"use strict";

import React from 'react';
import {getLoggedIn} from '../../../stores/users';
import Component from '../../../lib/component';
import Wrapper from '../../components/wrapper';

class AdminWrapper extends Component {

  componentDidMount() {
    const user = getLoggedIn();
    if (user && user.role !== 'admin') {
      this.redirectToDashboard();
    }
  }

  redirectToDashboard() {
    this.props.router.transitionTo('dashboard');
  }

  render() {
    return <Wrapper {...this.props} />
  }

}

AdminWrapper.propTypes = {
  router: React.PropTypes.func
};

export default AdminWrapper;