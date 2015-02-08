###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
RouteHandler = Router.RouteHandler
# components
Wrapper = require '../../../components/wrapper.coffee'
Subheader = require '../components/sub-header.coffee'

module.exports = React.createClass
    
    getInitialState: ->
        menu: [
            label: 'Outbox'
            route: 'messages-outbox'
        ,
            label: 'Sent'
            route: 'messages-sent'
        ,
            label: 'Compose'
            route: 'compose' 
        ]

    render: ->
        <Wrapper>
            <Subheader links={@state.menu} />
            <Wrapper />
        </Wrapper>