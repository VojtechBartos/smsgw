###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
ApplicationActions = require '../../../../actions/ApplicationActions.coffee'
ApplicationStore = require '../../../../stores/ApplicationStore.coffee'
# components
Table = require './../components/table.coffee'
Spinner = require '../../../components/spinner.coffee'

module.exports = React.createClass
    
    mixins: [ Router.Navigation ]

    getInitialState: ->
        pending: yes
        applications: []
        table: 
            options: [
                label: "Label", key: "label"
            ,
                label: "Prefix", key: "prefix"
            ,
                label: "Callback url", key: "callbackUrl"
            ,
                label: "Note", key: "note"
            ]
            actions: [
                label: 'Show', handler: @handleShowAction
            ,
                label: 'Delete', handler: @handleDeleteAction
            ]

    componentDidMount: ->
        ApplicationStore.addChangeListener @handleChange
        ApplicationActions.fetchAll()

    componentWillUnmount: ->
        ApplicationStore.removeChangeListener @handleChange

    handleChange: ->
        if @isMounted()
            @setState
                pending: no
                applications: ApplicationStore.getAll()

    handleShowAction: (app) ->
        @transitionTo 'application-overview', uuid: app.uuid

    handleDeleteAction: (app) ->
        @setState pending: yes
        ApplicationActions.delete app.uuid

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div id="context">
            <h1>
                Applications ({@state.applications.length}) 
                <Link to="application-add">Add</Link>
            </h1>
            <Table 
                options={@state.table.options} 
                items={@state.applications} 
                actions={@state.table.actions} />
        </div>