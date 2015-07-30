'use strict';

import React from 'react';
import {Map} from 'immutable';
import {get} from './actions';
import {flash} from '../flashMessages/actions';
import Component from '../components/component.react';
import Subheader from '../components/subheader.react';
import Spinner from '../components/spinner.react';

class Detail extends Component {

  componentDidMount() {
    get(this.uuid()).catch(err => {
      flash(err.message);

      this.redirectToList();
    });
  }

  uuid() {
    return this.props.router.getCurrentParams().uuid;
  }

  redirectToList() {
    this.props.router.transitionTo('phones');
  }

  render() {
    const phone = this.props.phones.get(this.uuid());

    if (get.pending || !phone)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <Subheader backTitle="Back" router={this.props.router}>
          <h1>{phone.hostname} ({phone.netName})</h1>
          <h2><strong>IMEI:</strong> {phone.imei}</h2>
        </Subheader>

        <div id="context">
          <strong>Client:</strong> {phone.client}<br />
          <strong>Network:</strong> {phone.netName}<br />
          <strong>Battery:</strong> {phone.battery}<br />
          <strong>Signal:</strong> {phone.signal}<br />
          <strong>Sent messages:</strong> {phone.sent}<br />
          <strong>Received messages:</strong> {phone.received}<br />
          <strong>Sending enabled:</strong> {String(phone.sendEnabled)}<br />
          <strong>Receiving enabled:</strong> {String(phone.receiveEnabled)}
        </div>
      </div>
    );
  }

}

Detail.propTypes = {
  router: React.PropTypes.func,
  phones: React.PropTypes.instanceOf(Map).isRequired
};

export default Detail;
