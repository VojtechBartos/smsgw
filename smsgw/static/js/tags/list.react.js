'use strict';

import React from 'react';
import {Link} from 'react-router';
import {Map} from 'immutable';
import * as actions from './actions';
import Component from '../components/component.react';
import Table from '../components/table.react';
import Spinner from '../components/spinner.react';

class List extends Component {

  componentDidMount() {
    actions.getAll();
  }

  onEditAction(tag) {
    this.props.router.transitionTo('tag-edit', {
      uuid: tag.uuid
    });
  }

  onDeleteAction(tag) {
    actions.remove(tag.uuid);
  }

  render() {
    if (actions.getAll.pending || actions.remove.pending)
      return <Spinner fullscreen={true} />;

    const tags = this.props.tags;
    const table = {
      options: [
        { label: 'Label', key: 'label' },
        { label: 'Note', key: 'note' },
        { label: 'Number of contacts', key: 'numberOfContacts' }
      ],
      actions: [
        { label: 'Edit', handler: this.onEditAction.bind(this) },
        { label: 'Delete', handler: this.onDeleteAction.bind(this) }
      ]
    };

    return (
      <div id="context">
        <h1>Tags ({tags.size}) <Link to="tag-add">Add</Link></h1>
        <Table options={table.options}
               items={tags}
               actions={table.actions} />
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  tags: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
