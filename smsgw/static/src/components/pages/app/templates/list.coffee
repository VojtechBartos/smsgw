###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
TemplateActions = require '../../../../actions/TemplateActions'
TemplateStore = require '../../../../stores/TemplateStore.coffee'
# components
Subheader = require './../components/sub-header.coffee'
Table = require './../components/table.coffee'
Spinner = require '../../../components/spinner.coffee'

module.exports = React.createClass

    mixins: [ Router.Navigation ]

    getInitialState: ->
        pending: no
        templates: []
        table:
            options: [
                label: "Label", key: "label"
            ,
                label: "Text", key: "text"
            ,
                label: "Created", key: "createdAt"
            ]
            actions: [
                label: 'Edit', handler: @handleEditAction
            ,
                label: 'Delete', handler: @handleDeleteAction
            ]

    componentDidMount: ->
        TemplateStore.addChangeListener @handleChange
        TemplateActions.fetchAll()

        @setState pending: yes

    componentWillUnmount: ->
        TemplateStore.removeChangeListener @handleChange

    handleChange: (data) ->
        if @isMounted()
            @setState
                pending: no
                templates: TemplateStore.getAll()

    handleEditAction: (template) ->
        @transitionTo 'template-edit', uuid: template.uuid

    handleDeleteAction: (template) ->
        @setState pending: yes
        TemplateActions.del template.uuid

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div>
            <div id="context">
                <h1>
                    Templates ({@state.templates.length})
                    <Link to="template-add">Add</Link>
                </h1>
                <Table
                    options={@state.table.options}
                    items={@state.templates}
                    actions={@state.table.actions} />
            </div>
        </div>
