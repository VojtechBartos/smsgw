###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
ContactActions = require '../../../../actions/ContactActions.coffee'
ContactStore = require '../../../../stores/ContactStore.coffee'
# components
Subheader = require './../components/sub-header.coffee'
Table = require './../components/table.coffee'
Spinner = require '../../../components/spinner.coffee'

module.exports = React.createClass
      
    mixins: [ Router.Navigation ]

    getInitialState: ->
        pending: no
        contacts: []
        menu: [
            label: 'Contacts'
            route: 'contacts'
        ,
            label: 'Tags'
            route: 'tags'   
        ]
        table: 
            options: [
                label: "Last name", key: "lastName"
            ,
                label: "First name", key: "firstName"
            ,
                label: "Phone number", key: "phoneNumber"
            ,   
                label: "Created", key: "createdAt"
            ]
            actions: [
                label: 'Edit', handler: @handleEditAction
            ,
                label: 'Delete', handler: @handleDeleteAction
            ]

    componentDidMount: ->
        # ContactStore.addChangeListener @handleChange
        # ContactActions.fetchAll()

        # @setState pending: yes

    componentWillUnmount: ->
        # ContactStore.removeChangeListener @handleChange

    handleChange: (data) ->
        # if @isMounted()
        #     @setState
        #         pending: no
        #         templates: ContactStore.getAll()

    handleEditAction: (template) ->
        # @transitionTo 'template-edit', uuid: template.uuid

    handleDeleteAction: (template) ->
        @setState pending: yes
        # ContactActions.delete template.uuid

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div>
            <Subheader links={@state.menu} />
            <div id="context">
                <h1>
                    Contacts ({@state.contacts.length}) 
                    <Link to="contact-add">Add</Link>
                </h1>
                <Table 
                    options={@state.table.options} 
                    items={@state.contacts} 
                    actions={@state.table.actions} />
            </div>
        </div>