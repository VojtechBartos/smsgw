###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
TagActions = require '../../../../../actions/TagActions.coffee'
TagStore = require '../../../../../stores/TagStore.coffee'
# components
Table = require './../../components/table.coffee'
Spinner = require '../../../../components/spinner.coffee'

module.exports = React.createClass
    
    mixins: [ Router.Navigation ]

    getInitialState: ->
        pending: no
        tags: []
        table: 
            options: [
                label: "Label", key: "label"
            ,
                label: "Note", key: "note"
            ,
                label: "Number of contacts", key: "numberOfContacts"
            ]
            actions: [
                label: 'Edit', handler: @handleEditAction
            ,
                label: 'Delete', handler: @handleDeleteAction
            ]

    componentDidMount: ->
        TagStore.addChangeListener @handleChange
        TagActions.fetchAll()

        @setState pending: yes

    componentWillUnmount: ->
        TagStore.removeChangeListener @handleChange

    handleChange: ->
        if @isMounted()
            @setState
                pending: no
                tags: TagStore.getAll()

    handleEditAction: (tag) ->
        @transitionTo 'tag-edit', uuid: tag.uuid

    handleDeleteAction: (tag) ->
        @setState pending: yes
        TagActions.delete tag.uuid

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div id="context">
            <h1>
                Tags ({@state.tags.length}) 
                <Link to="tag-add">Add</Link>
            </h1>
            <Table 
                options={@state.table.options} 
                items={@state.tags} 
                actions={@state.table.actions} />
        </div>