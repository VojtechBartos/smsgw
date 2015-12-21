'use strict';

import React from 'react';
import {Table, DropdownButton, MenuItem} from 'react-bootstrap';
import moment from 'moment';
import * as actions from './actions';
import * as store from './store';
import Component from '../components/component.react';
import Spinner from '../components/spinner.react';
import FlashMessages from '../components/flashmessages.react';
import Application from '../applications/application';


class List extends Component {

  componentDidMount() {
    const { application } = this.props;

    actions.getAll((application) ? application.uuid : null);
  }

  onViewAction(e, group) {
    e.preventDefault();

    const { application } = this.props;
    const route = (application) ? 'application-outbox-view' : 'outbox-view';

    this.props.router.transitionTo(route, {
      group: group.id,
      uuid: (application) ? application.uuid : null
    });
  }

  onDeleteAction(e, group) {
    e.preventDefault();

    const { application } = this.props;
    actions.remove(
      group.id,
      (application) ? application.uuid : null
    );
  }

  render() {
    const { application, flashMessages } = this.props;
    const groups = store.getAll((application) ? application.uuid : null);
    const now = moment();

    if (actions.getAll.pending || actions.remove.pending || !groups)
      return <Spinner fullscreen={true} />;

    return (
      <div id="context">
        <h1>Outbox ({groups.size})</h1>

        <FlashMessages messages={flashMessages} />

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
              return (
                <tr key={i}>
                  <td>{group.text}</td>
                  <td>{group.countOfRespondents}</td>
                  <td>{group.multiparts.length + 1}</td>
                  <td>
                    <div>
                      {group.sendLocalized} {''}
                      <small>
                        (in {moment.duration(group.sendDatetime.diff(now)).humanize()})
                      </small>
                    </div>
                  </td>
                  <td>{group.createdLocalized} {''}</td>
                  <td>
                    <DropdownButton title="actions"
                                    bsStyle="primary"
                                    bsSize="xsmall">
                      <MenuItem onClick={(e) => this.onViewAction(e, group)}>
                        View
                      </MenuItem>
                      <MenuItem onClick={(e) => this.onDeleteAction(e, group)}>
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
  application: React.PropTypes.instanceOf(Application)
};

export default List;
