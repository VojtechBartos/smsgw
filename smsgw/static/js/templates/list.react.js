"use strict";

import React from 'react';
import {Link} from 'react-router';
import {Map} from 'immutable';
import Component from '../components/component.react';
import * as actions from './actions';
import Spinner from '../components/spinner.react';
import Table from '../components/table.react';

class List extends Component {

  componentDidMount() {
    actions.getAll();
  }

  onEditAaction(template) {
    this.props.router.transitionTo('template-edit', {
      uuid: template.uuid
    });
  }

  onDeleteAction(template) {
    actions.remove(template.uuid);
  }

  render() {
    if (actions.getAll.pending || actions.remove.pending) {
      return <Spinner fullscreen={true} />;
    }

    const templates = this.props.templates;
    const table = {
      options: [
        { label: "Label", key: "label" },
        { label: "Text", key: "text" },
        { label: "Created", key: "createdAt" }
      ],
      actions: [
        { label: "Edit", handler: this.onEditAaction.bind(this) },
        { label: "Delete", handler: this.onDeleteAction.bind(this) }
      ]
    };

    return (
      <div>
        <div id="context">
          <h1>
              Templates ({templates.count()}) <Link to="template-add">Add</Link>
          </h1>
          <Table
              options={table.options}
              items={templates}
              actions={table.actions} />
        </div>
      </div>
    );
  }

}

List.propTypes = {
  router: React.PropTypes.func,
  templates: React.PropTypes.instanceOf(Map).isRequired
};

export default List;
