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
UserActions = require '../../../../actions/UserActions.coffee'

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

    handleUserMenu: (e) ->
        e.preventDefault()
        @setState userMenu: !@state.userMenu

    handleClickOnSide: ->
        @setState userMenu: no if @state.userMenu

    render: ->
        className = if @state.userMenu then 'opened' else null
        
        <header>
            <div id="logo"><strong>sms</strong>gw</div>
            <ul id="menu">  
                <li key="dashboard"><Link to="dashboard">dashboard</Link></li>
                <li key="applications"><Link to="applications">applications</Link></li>
                <li key="messages"><Link to="messages">messages</Link></li>
                <li key="templates"><Link to="templates">templates</Link></li>
                <li key="directory"><Link to="directory">directory</Link></li>
            </ul>
            <div className="user-menu">
                <a onClick={@handleUserMenu}>
                    <div className="info">
                        <div className="name">{@props.firstName} {@props.lastName}</div>
                        <div className="company">{@props.company}</div>
                    </div>
                    <div className="chevron" />
                </a>
                <ul className={className}>
                    <li key="email">vojta@sleepio.com</li>
                    <li key="settings"><Link to="settings">Settings</Link></li>
                    <li key="sign-out"><a onClick={@handleSignOut}>Sign out</a></li>
                </ul>
            </div>
            <div className="cleaner"/>
        </header>