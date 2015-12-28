'use strict';

import React from 'react';
import {Link} from 'react-router';
import Component from '../components/component.react';
import {signOut} from '../users/actions';
import {flash} from '../flashMessages/actions';

class Header extends Component {

  constructor(props) {
    super(props);
    this.state = {
      menu: false,
      mobileMenu: false
    };
  }

  signOut() {
    signOut();

    flash('Successfuly signed out.');

    this.props.router.transitionTo('signin');
  }

  onDesktopMenuClick(e) {
    e.preventDefault();
    if (!this.state.mobileMenu)
      this.setState({
        menu: !this.state.menu,
        mobileMenu: false
      });
  }

  onMobileMenuClick(e) {
    e.preventDefault();
    this.setState({
      menu: !this.state.mobileMenu,
      mobileMenu: !this.state.mobileMenu
    });
  }

  render() {
    let className = ['dropdown'];
    let mobileClassName = ['navbar-collapse', 'collapse'];
    if (this.state.menu)
      className.push('open');
    if (this.state.mobileMenu)
      mobileClassName.push('in');

    let menu = [
      'dashboard', 'applications', 'messages',
      'templates', 'directory'
    ];
    let user = {};
    if (this.props.user) {
      user = this.props.user;
      if (user.role === 'admin') {
        menu.push('users');
        menu.push('phones');
        menu.push('inbox');
      }
    }

    return (
      <nav className="navbar navbar-static-top">
        <div className="container-fluid">
            <Link to="dashboard" className="navbar-brand">
              <strong>sms</strong>gw
            </Link>

            <button type="button"
                    className="navbar-toggle collapsed"
                    onClick={e => this.onMobileMenuClick(e)}>
              <span className="sr-only">Toggle navigation</span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
              <span className="icon-bar"></span>
            </button>

            <div className={mobileClassName.join(' ')}>
              <ul className="nav navbar-nav">
                {menu.map(item => {
                  return <li key={item}><Link to={item}>{item}</Link></li>;
                })}
              </ul>
              <ul className="nav navbar-nav navbar-right">
                <li className={className.join(' ')}>
                  <a onClick={(e) => this.onDesktopMenuClick(e)}
                     className="dropdown-toggle"
                     role="button"
                     aria-expanded="false">
                    <div className="caret"></div>
                    <div className="info">
                      <div className="name">{user.firstName} {user.lastName}</div>
                      <div className="company">{user.company}</div>
                      <div className="cleaner" />
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
};

export default Header;
