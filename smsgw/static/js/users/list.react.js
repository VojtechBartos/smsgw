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

  onEditAction() {
    // TODO(vojta)
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
        { label: 'Created', key: 'createdAt' }
      ],
      actions: [

      ]
    };

    if (getAll.pending || !users)
      return <Spinner fullscreen={true} />;

    return (
      <div>
        <div id="context">
          <h1>Users ({users.size})</h1>
          <Table options={table.options}
                 items={users}
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
