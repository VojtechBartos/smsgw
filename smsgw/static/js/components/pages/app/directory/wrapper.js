"use strict";

import React from 'react';
import {RouteHandler} from 'react-router';
import Component from '../../../../lib/component';
import Wrapper from '../../../components/wrapper';
import Subheader from '../components/sub-header';

class DirectoryWrapper extends Component {

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

DirectoryWrapper.propTypes = {
  router: React.PropTypes.func
}

export default DirectoryWrapper;
