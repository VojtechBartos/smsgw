"use strict";

import React from 'react';
import {Link} from 'react-router';
import Component from '../components/component.react';
import {signOut} from '../users/actions';
import {flash} from '../flashMessages/actions';

class Header extends Component {

  constructor(props) {
    super(props);
    this.state = { menu: false };
  }

  componentDidMount() {
    document.body.addEventListener('click', this.onClickOutside.bind(this));
  }

  componentWillUnmount() {
    document.body.removeEventListener('click', this.onClickOutside);
  }

  signOut() {
    signOut();

    flash('Successfuly signed out.');

    this.props.router.transitionTo('signin');
  }

  onClick(e) {
    e.preventDefault();
    this.setState({ menu: !this.state.menu });
  }

  onClickOutside() {
    this.setState({ menu: false });
  }

  render() {
    let className = ['dropdown'];
    if (this.state.menu) {
      className.push('open');
    }

    let menu = [
      'dashboard', 'applications', 'messages',
      'templates', 'directory'
    ];
    let user = {};
    if (this.props.user) {
      user = this.props.user;
      if (user.role) {
        menu.push('users');
      }
    }

    return (
      <nav className="navbar navbar-static-top">
        <div className="container-fluid">
          <div id="navbar" className="navbar-collapse collapse">
            <Link to="dashboard" className="navbar-brand">
              <strong>sms</strong>gw
            </Link>
            <ul className="nav navbar-nav">
              {menu.map(item => {
                return <li key={item}><Link to={item}>{item}</Link></li>;
              })}
            </ul>
            <ul className="nav navbar-nav navbar-right">
              <li className={className.join(' ')}>
                <a onClick={(e) => this.onClick(e)}
                   className="dropdown-toggle"
                   role="button"
                   aria-expanded="false">
                  <div className="caret"></div>
                  <div className="info">
                    <div className="name">{user.firstName} {user.lastName}</div>
                    <div className="company">{user.company}</div>
                  </div>
                </a>
                <ul className="dropdown-menu" role="menu">
                  <li key="email" className="dropdown-header">{user.email}</li>
                  <li key="settings"><Link to="settings">Settings</Link></li>
                  <li className="divider"></li>
                  <li key="sign-out">
                    <a onClick={(e) => this.signOut(e)}>Sign out</a>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    );
  }

}

Header.propTypes = {
  router: React.PropTypes.func.isRequired
}

export default Header;
