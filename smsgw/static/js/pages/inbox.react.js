'use strict';

import React from 'react';
import Component from '../components/component.react';
import List from '../inbox/list.react';

class Inbox extends Component {

  render() {
    return <List {...this.props} user={null} />;
  }

}

export default Inbox;
