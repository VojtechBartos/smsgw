'use strict';

import React from 'react';
import Component from '../components/component.react';
import List from '../inbox/list.react';

class Inbox extends Component {

  render() {
    let props = this.props;
    props.user = null;

    return <List {...this.props} />;
  }

}

export default Inbox;
