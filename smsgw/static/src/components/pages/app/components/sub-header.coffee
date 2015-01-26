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

module.exports = React.createClass
    
    mixins: [Router.Navigation]

    getDefaultProps: ->
        backTitle: false,
        links: []

    handleBackInHistory: (e) ->
        e.preventDefault()
        window.history.back()

    render: ->
        links = []
        for link in @props.links
            links.push <Router.Link to={link.route}>{link.label}</Router.Link>

        backLink = null
        if @props.backTitle
            backLink = 
                <a className="back" onClick={@handleBackInHistory}>
                    <span className="chevron" />
                    {@props.backTitle}
                </a>
        
        <div id="subheader">
            {backLink}
            <div className="cleaner" />
            {@props.children}
            <div className="cleaner" />
            {links}
            <div className="cleaner" />
        </div>
