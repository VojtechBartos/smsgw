'use strict';

import React from 'react';
import {Link} from 'react-router';
import {Table, DropdownButton, MenuItem, Tooltip, OverlayTrigger} from 'react-bootstrap';
import {Map} from 'immutable';
import moment from 'moment';
import * as actions from './actions';
import * as store from './store';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';
import Application from '../applications/application';
import User from '../users/user';

class List extends Component {

  componentDidMount() {
    const { user, application } = this.props;

    actions.getAll(
      (user) ? user.uuid : null,
      (application) ? application.uuid : null
    );
  }

  onDeleteAction(e, message) {
    e.preventDefault();

    const { user, application } = this.props;
    actions.remove(
      message.uuid,
      (application) ? application.uuid : null,
      (user) ? user.uuid : null
    );
  }

  render() {
    const { application } = this.props;
    const sentItems = store.getAll((application) ? application.uuid : null);
    const now = moment();

    if (actions.getAll.pending || actions.remove.pending || !sentItems)
      return <Spinner fullscreen={true} />;

    return (
      <div id="context">
        <h1>Sent ({sentItems.size})</h1>

        <Table>
          <thead>
            <tr>
              <th>To</th>
              <th>Text</th>
              <th>Parts</th>
              <th>Sent at</th>
              <th>Created</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {sentItems.toArray().map((message, i) => {
              const contact = () => {
                if (!message.contact)
                  return message.destinationNumber;

                  const tooltip = <Tooltip>{message.contact.phoneNumber}</Tooltip>;
                  return (
                    <OverlayTrigger placement='right' overlay={tooltip}>
                      <Link to="contact-edit" params={{uuid: message.contact.uuid}}>
                        {message.contact.lastName} {message.contact.firstName}
                      </Link>
                    </OverlayTrigger>
                  );
              };

              return (
                <tr key={i}>
                  <td>{contact()}</td>
                  <td style={{maxWidth: '500px'}}>{message.text}</td>
                  <td>{message.multiparts}</td>
                  <td>
                    <div>
                      {message.sendLocalized} {' '}
                      <small>
                        ({moment.duration(message.sendDatetime.diff(now)).humanize()} ago)
                      </small>
                    </div>
                  </td>
                  <td>{message.createdLocalized}</td>
                  <td>
                    <DropdownButton id="dropdown-1"
                                    title="actions"
                                    bsStyle="primary"
                                    bsSize="xsmall">
                      <MenuItem eventKey="1"
                                onClick={(e) => this.onDeleteAction(e, message)}>
                        Delete
                      </MenuItem>
                    </DropdownButton>
                  </td>
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
  user: React.PropTypes.instanceOf(User),
  application: React.PropTypes.instanceOf(Application),
  sent: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
