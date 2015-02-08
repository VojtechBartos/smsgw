###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Dispatcher = require '../../../../dispatcher.coffee'
TemplateActions = require '../../../../actions/TemplateActions.coffee'
TemplateStore = require '../../../../stores/TemplateStore.coffee'
# components
TemplateForm = require './form.coffee'
FlashMessages = require '../../../components/flash-messages.coffee'
Subheader = require '../components/sub-header.coffee'

module.exports = React.createClass

    mixins: [ Router.Navigation ]

    getInitialState: ->
        formPending: no
        flashMessages: []

    componentDidMount: ->
        TemplateStore.addChangeListener @handleChange
        TemplateStore.addErrorListener @handleError

    componentWillUnmount: ->
        TemplateStore.removeChangeListener @handleChange
        TemplateStore.removeErrorListener @handleError

    handleChange: ->
        @transitionTo 'templates'

    handleError: (err) ->
        if @isMounted()
            @setState
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.templateForm
        if form.isValid()
            @setState formPending: yes
            TemplateActions.create form.getData()

    render: ->
        <div>
            <Subheader backTitle="Templates">
                <h1>Add template</h1>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <TemplateForm 
                    onSubmit={@handleSubmit} 
                    ref="templateForm"
                    pending={@state.formPending}
                    disabled={@state.formPending} />
            </div>
        </div>
