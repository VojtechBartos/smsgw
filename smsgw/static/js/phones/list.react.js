'use strict';

import React from 'react';
import {Table} from 'react-bootstrap';
import {Map} from 'immutable';
import moment from 'moment';
import * as actions from './actions';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';

class List extends Component {

  componentDidMount() {
    actions.getAll();
  }

  render() {
    const phones = this.props.phones;

    if (actions.getAll.pending || !phones)
      return <Spinner fullscreen={true} />;

    // TODO(vojta) add some detail view
    return (
      <div id="context">
        <h1>Phones ({phones.size})</h1>

        <Table>
          <thead>
            <tr>
              <th>Hostname</th>
              <th>Network</th>
              <th>Battery</th>
              <th>Signal</th>
              <th>Sent messages</th>
              <th>Received messages</th>
              <th>Last activity</th>
            </tr>
          </thead>
          <tbody>
            {phones.map((phone, i) => {
              return (
                <tr key={i}>
                  <td>{phone.hostname}</td>
                  <td>{phone.netName}</td>
                  <td>{phone.battery}%</td>
                  <td>{phone.signal}%</td>
                  <td>{phone.sent}</td>
                  <td>{phone.received}</td>
                  <td>{moment(phone.lastActivity).format('HH:mm DD.MM.YYYY')}</td>
                </tr>
              );
            })}
          </tbody>
        </Table>
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  phones: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
