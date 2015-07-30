'use strict';

import React from 'react';
import {Link} from 'react-router';
import {Map} from 'immutable';
import * as actions from './actions';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';
import Table from '../components/table.react';

class List extends Component {

  componentDidMount() {
    actions.getAll();
  }

  onEditAction(contact) {
    this.props.router.transitionTo('contact-edit', {
      uuid: contact.uuid
    });
  }

  onDeleteAction(contact) {
    actions.remove(contact.uuid);
  }

  render() {
    if (actions.getAll.pending || actions.remove.pending)
      return <Spinner fullscreen={true} />;

    const contacts = this.props.contacts;
    const table = {
      options: [
        { label: 'Last name', key: 'lastName' },
        { label: 'First name', key: 'firstName' },
        { label: 'Phone number', key: 'phoneNumber' },
        { label: 'Tags', key: 'tags' },
        { label: 'Created', key: 'createdAt' }
      ],
      actions: [
        { label: 'Edit', handler: this.onEditAction.bind(this) },
        { label: 'Delete', handler: this.onDeleteAction.bind(this) }
      ]
    };

    return (
      <div id="context">
        <h1>Contacts ({contacts.size}) <Link to="contact-add">Add</Link></h1>
        <Table options={table.options}
               items={contacts}
               actions={table.actions} />
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  contacts: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
