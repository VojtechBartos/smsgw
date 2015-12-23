'use strict';

import React from 'react';
import {Map} from 'immutable';
import {getAll, remove} from './actions';
import Component from '../components/component.react';
import Table from '../components/table.react';
import Spinner from '../components/spinner.react';

class List extends Component {

  componentDidMount() {
    getAll();
  }

  onEditAction(user) {
    this.props.router.transitionTo('user-edit', {
      uuid: user.uuid
    });
  }

  onDeleteAction(user) {
    remove(user.uuid);
  }

  render() {
    const users = this.props.users;
    const table = {
      options: [
        { label: 'Last name', key: 'lastName' },
        { label: 'Fisrt name', key: 'firstName' },
        { label: 'E-Mail', key: 'email' },
        { label: 'Company', key: 'company' },
        { label: 'Role', key: 'role' },
        { label: 'Active', key: 'isActive' },
        { label: 'Created', key: 'createdLocalized' }
      ],
      actions: [
        { label: 'Edit', handler: this.onEditAction.bind(this) },
        { label: 'Delete', handler: this.onDeleteAction.bind(this) }
      ]
    };

    if (getAll.pending || !users)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <div id="context">
          <h1>Users ({users.size})</h1>
          <Table options={table.options}
                 items={users.toArray()}
                 actions={table.actions} />
        </div>
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  users: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
