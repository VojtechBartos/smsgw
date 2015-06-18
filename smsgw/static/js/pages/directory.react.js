"use strict";

import React from 'react';
import {RouteHandler} from 'react-router';
import Component from '../components/component.react';
import Wrapper from '../components/wrapper.react';
import Subheader from '../components/subheader.react';

class Directory extends Component {

  render() {
    const menu = [
      { label: 'Contacts', route: 'contacts' },
      { label: 'Tags', route: 'tags' }
    ];

    return (
      <Wrapper>
        <Subheader router={this.props.router} links={menu} />
        <Wrapper {...this.props} />
      </Wrapper>
    );
  }

}

Directory.propTypes = {
  router: React.PropTypes.func
}

export default Directory;