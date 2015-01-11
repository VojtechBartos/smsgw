###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

# react libs
React = require 'react'
Router = require 'react-router'

module.exports = React.createClass
    
    mixins: [Router.Navigation]

    getDefaultProps: ->
        back: false,
        links: []

    handleBackInHistory: (e) ->
        e.preventDefault()
        window.history.back()

    render: ->
        links = []
        for link in @props.links
            links.push <Router.Link to={link.route}>{link.label}</Router.Link>

        back = null
        if @props.back
            back = <a href="#" onClick={@handleBackInHistory}>< Back</a>
        

        <div id="subheader">
            {back}
            {links}
        </div>
