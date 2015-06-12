"use strict";

import React from 'react';
import {Map} from 'immutable';
import {flash} from '../../../../actions/flashMessages';
import * as actions from '../../../../actions/applications';
import * as store from '../../../../stores/applications';
import Component from '../../../../lib/component';
import Wrapper from '../../../components/wrapper';
import Subheader from '../components/sub-header';
import Spinner from '../../../components/spinner';

class ApplicationWrapper extends Component {

  componentDidMount() {
    actions.get(this.uuid()).error((err) => {
      flash('Application not found.');

      this.redirectToList();
    });
  }

  uuid() {
    return this.props.router.getCurrentParams().uuid;
  }

  redirectToList() {
    this.props.router.replaceWith('applications');
  }

  onRegenerateClick() {
    actions.regenerateToken(this.uuid());
  }

  render() {
    const app = store.get(this.uuid());
    const params = this.props.router.getCurrentParams();
    const menu = [
      {
        label: 'Overview',
        route: 'application-overview',
        params
      },
      {
        label: 'Settings',
        route: 'application-settings',
        params
      },
      {
        label: 'Sent messages',
        route: 'application-sent-messages',
        params
      },
      {
        label: 'Received messages',
        route: 'application-received-messages',
        params
      }
    ];

    if (actions.get.pending || actions.regenerateToken.pending || !app) {
      return <Spinner fullscreen={true} />;
    }

    return (
      <Wrapper>
        <Subheader backTitle="Applications"
                   backRoute="applications"
                   links={menu}
                   router={this.props.router}>
          <h1>{app.label}</h1>
          <h3>
            <strong><small>API Key: </small></strong>
            {app.token}{" "}
            <a className="small" onClick={e => this.onRegenerateClick(e)}>
              regenerate
            </a>
          </h3>
        </Subheader>
        <Wrapper application={app} {...this.props} />
      </Wrapper>
    );
  }

}

ApplicationWrapper.propTypes = {
  router: React.PropTypes.func,
  applications: React.PropTypes.instanceOf(Map).isRequired
};

export default ApplicationWrapper;

