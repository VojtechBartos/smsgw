###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
TemplateActions = require '../../../../actions/TemplateActions'
TemplateStore = require '../../../../stores/TemplateStore.coffee'
# components
TemplateForm = require './form.coffee'
FlashMessages = require '../../../components/flash-messages.coffee'
Subheader = require '../components/sub-header.coffee'
Spinner = require '../../../components/spinner.coffee'

module.exports = React.createClass

    mixins: [Router.Navigation, Router.State]

    getInitialState: ->
        pending: no
        formPending: no
        flashMessages: []
        template:
            label: null

    componentDidMount: ->
        TemplateStore.addChangeListener @handleChange
        TemplateStore.addErrorListener @handleError

        TemplateActions.fetch @getParams().uuid
        @setState pending: yes

    componentWillUnmount: ->
        TemplateStore.removeChangeListener @handleChange
        TemplateStore.removeErrorListener @handleError

    handleChange: (data) ->
        if @isMounted()
            @setState
                pending: no
                formPending: no
                template: TemplateStore.get @getParams().uuid
                flashMessages: []

    handleError: (err) ->
        if @isMounted()
            @setState
                pending: no
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.templateForm
        if form.isValid()
            @setState formPending: yes
            TemplateActions.update @state.template.uuid, form.getData()

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div>
            <Subheader backTitle="Templates">
                <h1>{@state.template.label}</h1>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <TemplateForm
                    onSubmit={@handleSubmit}
                    ref="templateForm"
                    pending={@state.formPending}
                    disabled={@state.formPending}
                    submitTitle="Edit"
                    data={@state.template} />
            </div>
        </div>
