'use strict';

import React from 'react';
import Component from './component.react';

class AutocompleteInput extends Component {

  onChange(e) {
    if (this.props.onChange)
      this.props.onChange(e.target.value);
  }

  onSelect(item) {
    return () => {
      this.refs.getDOMNode().value = '';
      if (this.props.onSelect)
        this.props.onSelect(item);
    };
  }

  render() {
    const classNamespace = this.props.classNamespace;
    const options = this.props.options;
    const throbber = []; // TODO(vojta)

    return (
      <div className={classNamespace}>
        <input type="text"
               ref='text'
               className="form-control"
               onChange={e => this.onChange(e)} />
        <div className={throbber.join(' ')} />
        <div className="cleaner" />
        <ul className="options">
          {options.map((option) => {
            return (
              <li onClick={() => this.onSelect(option)}>
                {option.label}
              </li>
            );
          })}
        </ul>
      </div>
    );
  }

}

export default AutocompleteInput;
