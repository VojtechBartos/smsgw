###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Dispatcher = require '../../../../../dispatcher.coffee'
ApplicationActions = require '../../../../../actions/ApplicationActions.coffee'
ApplicationStore = require '../../../../../stores/ApplicationStore.coffee'
# components
ApplicationForm = require '../form.coffee'
FlashMessages = require '../../../../components/flash-messages.coffee'

module.exports = React.createClass

    getInitialState: ->
        formPending: no
        flashMessages: []

    componentDidMount: ->
        ApplicationStore.addChangeListener @handleChange
        ApplicationStore.addErrorListener @handleError

    componentWillUnmount: ->
        ApplicationStore.removeChangeListener @handleChange
        ApplicationStore.removeErrorListener @handleError

    handleChange: (data) ->
        @setState formPending: no if @isMounted()

    handleError: (err) ->
        if @isMounted()
            @setState
                formPending: no
                flashMessages: [text: err.message, type: 'alert']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.applicationForm
        if form.isValid()
            @setState formPending: yes
            ApplicationActions.update @props.application.uuid, form.getData()

    render: ->
        <div id="context">
            <FlashMessages messages={@state.flashMessages} />

            <ApplicationForm 
                onSubmit={@handleSubmit} 
                ref="applicationForm"
                submitTitle="Save"
                pending={@state.formPending}
                disabled={@state.formPending}
                data={@props.application} />
        </div>