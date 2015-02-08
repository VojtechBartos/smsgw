###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Dispatcher = require '../../../../../dispatcher.coffee'
TagActions = require '../../../../../actions/TagActions.coffee'
TagStore = require '../../../../../stores/TagStore.coffee'
# components
TagForm = require './form.coffee'
FlashMessages = require '../../../../components/flash-messages.coffee'
Subheader = require '../../components/sub-header.coffee'
Spinner = require '../../../../components/spinner.coffee'

module.exports = React.createClass

    mixins: [Router.Navigation, Router.State]

    getInitialState: ->
        pending: no
        formPending: no
        flashMessages: []
        tag: 
            label: null

    componentDidMount: ->
        TagStore.addChangeListener @handleChange
        TagStore.addErrorListener @handleError

        TagActions.fetch @getParams().uuid
        @setState pending: yes

    componentWillUnmount: ->
        TagStore.removeChangeListener @handleChange
        TagStore.removeErrorListener @handleError

    handleChange: (data) ->
        if @isMounted()
            @setState
                pending: no
                formPending: no
                tag: TagStore.get @getParams().uuid
                flashMessages: []

    handleError: (err) ->
        if @isMounted()
            @setState
                pending: no
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.tagForm
        if form.isValid()
            @setState formPending: yes
            TagActions.update @state.tag.uuid, form.getData()

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div>
            <Subheader backTitle="Tags" backRoute="tags">
                <h1>{@state.tag.label}</h1>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <TagForm 
                    onSubmit={@handleSubmit} 
                    ref="tagForm"
                    pending={@state.formPending}
                    disabled={@state.formPending} 
                    submitTitle="Edit"
                    data={@state.tag} />
            </div>
        </div>