'use strict';

import React from 'react';
import {Link} from 'react-router';

class Subheader extends React.Component {

  onBackInHistory(e) {
    e.preventDefault();

    if (this.props.backRoute)
      this.props.router.replaceWith(this.props.backRoute);
    else
      window.history.back();
  }

  render() {
    let back = null;
    if (this.props.backTitle)
      back = (
        <a className="back" onClick={e => this.onBackInHistory(e)}>
          <span className="chevron" />
          {this.props.backTitle}
        </a>
      );

    return (
      <div id="subheader">
        {back}
        <div className="cleaner" />
        {this.props.children}
        <div className="cleaner" />
        {this.props.links.map((link, index) => {
          return (
            <Link to={link.route} key={index} params={link.params}>
              {link.label}
            </Link>
          );
        })}
        <div className="cleaner" />
      </div>
    );
  }

}

Subheader.defaultProps = {
  links: []
};

Subheader.propTypes = {
  router: React.PropTypes.func.isRequired,
  backTitle: React.PropTypes.string,
  backRoute: React.PropTypes.string,
  link: React.PropTypes.array
};

export default Subheader;
