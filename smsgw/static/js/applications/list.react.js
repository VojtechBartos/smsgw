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

  onShowAction(app) {
    this.props.router.transitionTo('application-overview', {
      uuid: app.uuid
    });
  }

  onDeleteAction(app) {
    actions.remove(app.uuid);
  }

  render() {
    if (actions.getAll.pending || actions.remove.pending)
      return <Spinner fullscreen={true} />;

    const apps = this.props.applications;
    const table = {
      options: [
        { label: 'Label', key: 'label' },
        { label: 'Prefix', key: 'prefix' },
        { label: 'Callback url', key: 'callbackUrl' },
        { label: 'Note', key: 'note' },
        { label: 'Created', key: 'createdLocalized' }
      ],
      actions: [
        { label: 'Show', handler: this.onShowAction.bind(this) },
        { label: 'Delete', handler: this.onDeleteAction.bind(this) }
      ]
    };

    return (
      <div id="context">
        <h1>
          Applications ({apps.size}) <Link to="application-add">Add</Link>
        </h1>
        <Table options={table.options}
               items={apps.toArray()}
               actions={table.actions} />
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  templates: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
