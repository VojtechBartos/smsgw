###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
RouteHandler = Router.RouteHandler
ApplicationStore = require '../../../../stores/ApplicationStore.coffee'
ApplicationActions = require '../../../../actions/ApplicationActions'
# components
Wrapper = require '../../../components/wrapper.coffee'
Subheader = require '../components/sub-header.coffee'
Spinner = require '../../../components/spinner.coffee'

module.exports = React.createClass

    mixins: [ Router.State ]

    getInitialState: ->
        pending: yes
        application: ApplicationStore.get @getParams().uuid
        menu: [
            label: 'Overview'
            route: 'application-overview'
            params: @getParams()
        ,
            label: 'Settings'
            route: 'application-settings'
            params: @getParams()
        ,
            label: 'Sent messages'
            route: 'application-sent-messages'
            params: @getParams()
        ,
            label: 'Received messages'
            route: 'application-received-messages'
            params: @getParams()
        ]

    componentDidMount: ->
        ApplicationStore.addChangeListener @handleChange
        ApplicationActions.fetch @getParams().uuid if not @state.application?
        @setState pending: not @state.application?

    componentWillUnmount: ->
        ApplicationStore.removeChangeListener @handleChange

    handleChange: ->
        if @isMounted()
            @setState
                pending: no
                application: ApplicationStore.get @getParams().uuid

    handleRegenerate: ->
        @setState pending: yes
        ApplicationActions.regenerateToken @getParams().uuid

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <Wrapper>
            <Subheader
                backTitle="Applications"
                backRoute="applications"
                links={@state.menu}>
                <h1>{@state.application.label}</h1>
                <h3>
                    <strong><small>API Key: </small></strong>
                    {@state.application.token}{" "}
                    <a className="small" onClick={@handleRegenerate}>regenerate</a>
                </h3>
            </Subheader>
            <Wrapper application={@state.application} />
        </Wrapper>
