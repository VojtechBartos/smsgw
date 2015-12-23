'use strict';

import React from 'react';
import {Link} from 'react-router';
import {Table, DropdownButton, MenuItem, Tooltip, OverlayTrigger} from 'react-bootstrap';
import Immutable from 'immutable';
import moment from 'moment';
import * as actions from './actions';
import * as store from './store';
import Component from '../components/component.react';
import FlashMessages from '../components/flashmessages.react';
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
    const { application, flashMessages } = this.props;
    const inbox = store.getAll((application) ? application.uuid : null);
    const now = moment();

    if (actions.getAll.pending || actions.remove.pending || !inbox)
      return <Spinner fullscreen={true} />;

    return (
      <div id="context">
        <h1>Inbox ({inbox.size})</h1>

        <FlashMessages messages={flashMessages} />

        <Table>
          <thead>
            <tr>
              <th>From</th>
              <th>Text</th>
              <th>Received at</th>
              <th>Created</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {inbox.toArray().map((message, i) => {
              const contact = () => {
                if (!message.contact)
                  return message.senderNumber;

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
                  <td>
                    <div>
                      {message.receivedLocalized} {' '}
                      <small>
                        ({moment.duration(message.receivedDatetime.diff(now)).humanize()} ago)
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
  flashMessages: React.PropTypes.instanceOf(Immutable.List).isRequired,
  user: React.PropTypes.instanceOf(User),
  application: React.PropTypes.instanceOf(Application),
  sent: React.PropTypes.instanceOf(Immutable.Map).isRequired
};

export default List;
