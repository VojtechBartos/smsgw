'use strict';

import React from 'react';
import {RouteHandler} from 'react-router';

class Wrapper extends React.Component {

  render() {
    const style = {
      position: 'relative',
      height: '100%',
      width: '100%'
    };

    return (
      <div style={style}>
        {(function(props) {
          // TODO(vojta) rewrite to ES6 closure syntax
          var content = props.children;
          if (!content)
            content = <RouteHandler {...props} />;
          return content;
        })(this.props)}
      </div>
    );
  }

}

export default Wrapper;
