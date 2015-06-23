'use strict';

import React from 'react';
import {Alert} from 'react-bootstrap';
import Immutable from 'immutable';
import Component from './component.react';

class FlashMessages extends Component {

  render() {
    const messages = this.props.messages;

    return (
      <div className="flashes">
        {messages.map((message, index) => {
          return (
            <Alert key={index} bsStyle={message.type}>
              {message.text}
            </Alert>
          );
        })}
      </div>
    );
  }

}

FlashMessages.propTypes = {
  messages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default FlashMessages;
