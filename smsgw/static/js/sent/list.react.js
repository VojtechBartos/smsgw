'use strict';

import React from 'react';
import {Link} from 'react-router';
import {Table, DropdownButton, MenuItem} from 'react-bootstrap';
import {Map} from 'immutable';
import moment from 'moment';
import * as actions from './actions';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';

class List extends Component {

  componentDidMount() {
    actions.getAll();
  }

  onDeleteAction(e, message) {
    e.preventDefault();

    actions.remove(message.id);
  }

  render() {
    const sentItems = this.props.sent;

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
              <th>Sending at</th>
              <th>Created</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {sentItems.map((message, i) => {
              const contact = () => {
                if (!message.contact)
                  return message.destinationNumber;

                return (
                  <Link to="contact-edit"
                        params={{uuid: message.contact.uuid}}>
                    {message.contact.lastName} {message.contact.firstName}
                  </Link>
                );
              };
              const send = () => {
                if (!message.send) return;
                // const dt = moment(message.send);
                // "#{dt.format 'HH:mm DD.MM.YYYY'} (#{dt.from moment()})"
                // return `TODO(vojta)`;
              };

              return (
                <tr key={i}>
                  <td>{contact()}</td>
                  <td>{message.text}</td>
                  <td>{send()}</td>
                  <td>{moment(message.created).format('HH:mm DD.MM.YYYY')}</td>
                  <td>
                    <DropdownButton title="actions"
                                    bsStyle="primary"
                                    bsSize="xsmall">
                      <MenuItem eventKey="1">Edit</MenuItem>
                      <MenuItem eventKey="2"
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
  sent: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
