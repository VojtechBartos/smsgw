###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Dispatcher = require '../../../../dispatcher.coffee'
ApplicationActions = require '../../../../actions/ApplicationActions.coffee'
ApplicationStore = require '../../../../stores/ApplicationStore.coffee'
# components
ApplicationForm = require './form.coffee'
FlashMessages = require '../../../components/flash-messages.coffee'
Subheader = require '../components/sub-header.coffee'

module.exports = React.createClass
    
    mixins: [ Router.Navigation ]

    getInitialState: ->
        formPending: no
        flashMessages: []

    componentDidMount: ->
        ApplicationStore.addChangeListener @handleChange
        ApplicationStore.addErrorListener @handleError

    componentWillUnmount: ->
        ApplicationStore.removeChangeListener @handleChange
        ApplicationStore.removeErrorListener @handleError

    handleChange: ->
        @transitionTo 'applications'

    handleError: (err) ->
        if @isMounted()
            @setState
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.applicationForm
        if form.isValid()
            @setState formPending: yes
            ApplicationActions.create form.getData()

    render: ->
        <div>
            <Subheader backTitle="Applications" backRoute="applications">
                <h1>Add application</h1>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <ApplicationForm 
                    onSubmit={@handleSubmit} 
                    ref="applicationForm"
                    pending={@state.formPending}
                    disabled={@state.formPending} />
            </div>
        </div>