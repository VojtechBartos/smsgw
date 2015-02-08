###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
UserActions = require '../../../../actions/UserActions.coffee'
UserStore = require '../../../../stores/UserStore.coffee'
# components
Subheader = require './../components/sub-header.coffee'
Table = require './../components/table.coffee'
Spinner = require '../../../components/spinner.coffee'

module.exports = React.createClass
      
    mixins: [ Router.Navigation ]

    getInitialState: ->
        pending: no
        users: UserStore.getAll()
        table: 
            options: [
                label: "Last name", key: "lastName"
            ,
                label: "First name", key: "firstName"
            ,
                label: "E-Mail", key: "email"
            ,
                label: "Company", key: "company"
            ,
                label: "Role", key: "role"
            ,
                label: "Active", key: "isActive"
            ,
                label: "Created", key: "createdAt"
            ]
            actions: [
                label: 'Edit', handler: @handleEditAction
            ,
                label: 'Delete', handler: @handleDeleteAction
            ]

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        UserActions.fetchAll()

        @setState pending: yes

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange

    handleChange: ->
        @setState
            pending: no
            users: UserStore.getAll()

    handleEditAction: (template) ->
        # @transitionTo 'template-edit', uuid: template.uuid

    handleDeleteAction: (template) ->
        @setState pending: yes
        UserActions.delete template.uuid

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div>
            <div id="context">
                <h1>
                    Users ({@state.users.length}) 
                </h1>
                <Table 
                    options={@state.table.options} 
                    items={@state.users} 
                    actions={@state.table.actions} />
            </div>
        </div>