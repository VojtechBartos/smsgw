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
    
    mixins: [ Router.State ]

    getInitialState: ->
        menu: [
            label: 'Overview'
            route: 'application-overview'
            params: @getParams()
        ,
            label: 'Settings'
            route: 'application-settings'
            params: @getParams()
        ,
            label: 'Messages'
            route: 'application-messages'   
            params: @getParams()
        ]

    render: ->
        <Wrapper>
            <Subheader 
                backTitle="Applications" 
                backRoute="applications" 
                links={@state.menu}>
                <h1>cenolom.cz</h1>
            </Subheader>
            <Wrapper />
        </Wrapper>