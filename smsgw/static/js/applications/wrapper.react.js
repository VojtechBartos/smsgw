'use strict';

import React from 'react';
import {Map} from 'immutable';
import {flash} from '../flashMessages/actions';
import * as actions from './actions';
import * as store from './store';
import Component from '../components/component.react';
import Wrapper from '../components/wrapper.react';
import Subheader from '../components/subheader.react';
import Spinner from '../components/spinner.react';

class ApplicationWrapper extends Component {

  componentDidMount() {
    actions.get(this.uuid()).error((err) => {
      flash(err.message);

      this.redirectToList();
    });
  }

  uuid() {
    return this.props.router.getCurrentParams().uuid;
  }

  redirectToList() {
    this.props.router.transitionTo('applications');
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
        label: 'Outbox',
        route: 'application-outbox',
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

    if (actions.get.pending || actions.regenerateToken.pending || !app)
      return <Spinner fullscreen={true} />;

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
