"use strict";

import React from 'react';
import shallowEqual from 'react-pure-render/shallowEqual';

class Component extends React.Component {

  shouldComponentUpdate(nextProps, nextState) {
    // TODO: Make whole React Pure, add something like dangerouslySetLocalState.
    // https://github.com/gaearon/react-pure-render#known-issues
    // https://twitter.com/steida/status/600395820295450624
    if (this.context.router) {
      const changed = this.pureComponentLastPath !== this.context.router.getCurrentPath();
      this.pureComponentLastPath = this.context.router.getCurrentPath();
      if (changed) return true;
    }

    return !shallowEqual(this.props, nextProps) ||
           !shallowEqual(this.state, nextState);
  }

}

Component.contextTypes = {
  router: React.PropTypes.func
};

export default Component;
