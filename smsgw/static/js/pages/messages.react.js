'use strict';

import React from 'react';
import Component from '../components/component.react';
import Wrapper from '../components/wrapper.react';
import Subheader from '../components/subheader.react';

class MessagesWrapper extends Component {

  render() {
    const menu = [
      { label: 'Outbox', route: 'outbox' },
      { label: 'Sent', route: 'sent' },
      { label: 'Compose', route: 'compose' }
    ];

    return (
      <Wrapper>
        <Subheader router={this.props.router} links={menu} />
        <Wrapper {...this.props} />
      </Wrapper>
    );
  }

}

MessagesWrapper.propTypes = {
  router: React.PropTypes.func
};

export default MessagesWrapper;
