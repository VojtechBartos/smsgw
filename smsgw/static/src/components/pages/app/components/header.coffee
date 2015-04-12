###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

# react libs
React = require 'react'
Router = require 'react-router'
Link = Router.Link
UserActions = require '../../../../actions/UserActions'

module.exports = React.createClass

    mixins: [Router.Navigation]

    getInitialState: ->
        userMenu: no

    componentDidMount: ->
        document.body.addEventListener 'click', @handleClickOnSide

    componentWillUnmount: ->
        document.body.removeEventListener 'click', @handleClickOnSide

    handleSignOut: ->
        UserActions.signOut()
        @transitionTo 'sign-in'

    handleClick: (e) ->
        e.preventDefault()
        @setState userMenu: !@state.userMenu

    handleClickOnSide: ->
        @setState userMenu: no if @state.userMenu

    render: ->
        className = ['dropdown']
        className.push 'open' if @state.userMenu

        users = null
        if @props.user.role == 'admin'
            users = <li key="users"><Link to="users">users</Link></li>

        <nav className="navbar navbar-static-top">
            <div className="container-fluid">
                <div id="navbar" className="navbar-collapse collapse">
                    <Link to="dashboard" className="navbar-brand">
                        <strong>sms</strong>gw
                    </Link>
                    <ul className="nav navbar-nav">
                        <li key="dashboard"><Link to="dashboard">dashboard</Link></li>
                        <li key="applications"><Link to="applications">applications</Link></li>
                        <li key="messages"><Link to="messages">messages</Link></li>
                        <li key="templates"><Link to="templates">templates</Link></li>
                        <li key="directory"><Link to="directory">directory</Link></li>
                        {users}
                    </ul>
                    <ul className="nav navbar-nav navbar-right">
                        <li className={className.join ' '}>
                            <a onClick={@handleClick} className="dropdown-toggle" role="button" aria-expanded="false">
                                <div className="caret"></div>
                                <div className="info">
                                    <div className="name">
                                        {@props.user.firstName} {@props.user.lastName}
                                    </div>
                                    <div className="company">{@props.user.company}</div>
                                </div>
                            </a>
                            <ul className="dropdown-menu" role="menu">
                                <li key="email" className="dropdown-header">vojta@sleepio.com</li>
                                <li key="settings"><Link to="settings">Settings</Link></li>
                                <li className="divider"></li>
                                <li key="sign-out"><a onClick={@handleSignOut}>Sign out</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
