"use strict";

import React from 'react';
import Component from '../../../../lib/component';
import Wrapper from '../../../components/wrapper';
import Subheader from '../components/sub-header';

class MessagesWrapper extends Component {

  render() {
    const menu = [
      { label: 'Outbox', route: 'messages-outbox' },
      { label: 'Sent', route: 'messages-sent' },
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
}

export default MessagesWrapper;
