"use strict";

import React from 'react';

class Spinner extends React.Component {

  render() {
    let classNames = ['spinner'];
    if (this.props.fullscreen) {
      classNames.push('fullscreen');
    }

    return (
      <div className={classNames.join(' ')}>
        <div className="dots">
          Loading ...
        </div>
      </div>
    );
  }

}

Spinner.defaultProps = {
  fullscreen: false
};

Spinner.propTypes = {
  fullscreen: React.PropTypes.bool
};

export default Spinner;
