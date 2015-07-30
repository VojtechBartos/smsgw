'use strict';

import React from 'react';
import {Table, DropdownButton, MenuItem} from 'react-bootstrap';
import {Map} from 'immutable';
import * as actions from './actions';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';

class Outbox extends Component {

  componentDidMount() {
    actions.getAll();
  }

  onDeleteAction(e, group) {
    e.preventDefault();

    actions.remove(group.id);
  }

  render() {
    const groups = this.props.outboxGroups;

    if (actions.getAll.pending || actions.remove.pending || !groups)
      return <Spinner fullscreen={true} />;

    return (
      <div id="context">
        <h1>Outbox ({groups.size})</h1>

        <Table>
          <thead>
            <tr>
              <th>Text</th>
              <th>Respondents</th>
              <th>Parts</th>
              <th>Sending at</th>
              <th>Created</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            {groups.map((group, i) => {
              let text = group.message;
              if (text && group.multiparts.length > 0)
                text += ' ...';

              return (
                <tr key={i}>
                  <td>{text}</td>
                  <td>{group.countOfRespondents}</td>
                  <td>{group.multiparts.length + 1}</td>
                  <td>{group.send}</td>
                  <td>{group.created}</td>
                  <td>
                    <DropdownButton title="actions"
                                    bsStyle="primary"
                                    bsSize="xsmall">
                      <MenuItem eventKey="1">Edit</MenuItem>
                      <MenuItem eventKey="2"
                                onClick={(e) => this.onDeleteAction(e, group)}>
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

Outbox.propTypes = {
  router: React.PropTypes.func,
  outboxGroups: React.PropTypes.instanceOf(Map).isRequired
};

export default Outbox;
