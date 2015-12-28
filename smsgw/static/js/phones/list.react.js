'use strict';

import React from 'react';
import {Table, DropdownButton, MenuItem} from 'react-bootstrap';
import Immutable from 'immutable';
import moment from 'moment';
import {getAll} from './actions';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
import Spinner from '../components/spinner.react';

class List extends Component {

  componentDidMount() {
    getAll();
  }

  onShowAction(phone) {
    this.props.router.transitionTo('phone-detail', {
      uuid: phone.uuid
    });
  }

  render() {
    const { phones, flashMessages } = this.props;
    const now = moment();

    if (getAll.pending || !phones)
      return <Spinner fullscreen={true} />;

    return (
      <div id="context">
        <h1>Phones ({phones.size})</h1>

        <FlashMessages messages={flashMessages} />

        <Table responsive>
          <thead>
            <tr>
              <th>Hostname</th>
              <th>Network</th>
              <th>Battery</th>
              <th>Signal</th>
              <th>Sent messages</th>
              <th>Received messages</th>
              <th>Last activity</th>
              <th>Created</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {phones.toArray().map((phone, i) =>
              <tr key={i}>
                <td>{phone.hostname}</td>
                <td>{phone.netName}</td>
                <td>{phone.battery}%</td>
                <td>{phone.signal}%</td>
                <td>{phone.sent}</td>
                <td>{phone.received}</td>
                <td>
                  <div>
                    {phone.lastActivityLocalized} {' '}
                    <small>
                      ({moment.duration(phone.lastActivityDatetime.diff(now)).humanize()} ago)
                    </small>
                  </div>
                </td>
                <td>{phone.createdLocalized}</td>
                <td>
                  <DropdownButton id="dropdown-1"
                                  title="actions"
                                  bsStyle="primary"
                                  bsSize="xsmall">
                    <MenuItem onClick={() => this.onShowAction(phone)}>
                      Show
                    </MenuItem>
                  </DropdownButton>
                </td>
              </tr>
            )}
          </tbody>
        </Table>
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  phones: React.PropTypes.instanceOf(Immutable.Map).isRequired,
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired
};

export default List;
