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


Menu = React.createClass
    render: ->
        <ul id="menu">  
            <li><Link to="dashboard">dashboard</Link></li>
            <li><Link to="applications">applications</Link></li>
            <li><Link to="messages">messages</Link></li>
            <li><Link to="templates">templates</Link></li>
            <li><Link to="contacts">contacts</Link></li>
        </ul>

Header = React.createClass
    render: ->
        <header>
            <div id="logo"><strong>sms</strong>gw</div>
            <Menu />
            <div className="user-menu">
                <a href="#">
                    <div className="info">
                        <div className="name">Vojtech Bartos</div>
                        <div className="company">alinet.cz</div>
                    </div>
                    <div className="chevron" />
                </a>
            </div>
            <div className="cleaner"/>
        </header>

module.exports = Header