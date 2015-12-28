'use strict';

import _ from 'lodash';
import React from 'react';
import {Table, Label, DropdownButton, MenuItem} from 'react-bootstrap';


class CustomTable extends React.Component {

  onAction(action, item) {
    return (e) => {
      e.preventDefault();
      action.handler(item);
    };
  }

  render() {
    const options = this.props.options;
    const items = this.props.items;
    const actions = this.props.actions;

    return (
      <Table responsive>
        <thead>
          <tr>
            {options.map(option =>
              <th key={option.key}>{option.label}</th>
            )}
            <th key="actions">Actions</th>
          </tr>
        </thead>
        <tbody>
          {items.map((item, i) =>
            <tr key={i}>
              {options.map(option => {
                let value = item[option.key];
                let content = [];
                if (_.isBoolean(value))
                  content = (
                    <Label bsStyle={(value) ? 'success' : 'danger'}>
                      {(value) ? 'yes' : 'no'}
                    </Label>
                  );
                else if (_.isArray(value))
                  value.forEach((i) => {
                    content.push(<Label key={i} bsStyle="info">{i}</Label>);
                  });
                else content = value;

                return <td key={option.key}>{content}</td>;
              })}
              <td key="actions">
                <DropdownButton id="dropdown-1"
                                title="actions"
                                bsStyle="primary"
                                bsSize="xsmall">
                  {actions.map((action, j) => {
                    return (
                      <MenuItem key={j} eventKey={j}
                                onClick={this.onAction(action, item)}>
                        {action.label}
                      </MenuItem>
                    );
                  })}
                </DropdownButton>
              </td>
            </tr>
          )}
        </tbody>
      </Table>
    );
  }

}

CustomTable.defaultProps = {
  options: [],
  items: [],
  actions: []
};

export default CustomTable;
