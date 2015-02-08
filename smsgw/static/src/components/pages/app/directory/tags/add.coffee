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

module.exports = React.createClass
    
    mixins: [ Router.Navigation ]

    getInitialState: ->
        formPending: no
        flashMessages: []

    componentDidMount: ->
        TagStore.addChangeListener @handleChange
        TagStore.addErrorListener @handleError

    componentWillUnmount: ->
        TagStore.removeChangeListener @handleChange
        TagStore.removeErrorListener @handleError

    handleChange: ->
        @transitionTo 'tags'

    handleError: (err) ->
        if @isMounted()
            @setState
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.tagForm
        if form.isValid()
            @setState formPending: yes
            TagActions.create form.getData()

    render: ->
        <div>
            <Subheader backTitle="Tags" backRoute="tags">
                <h1>Add tag</h1>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <TagForm 
                    onSubmit={@handleSubmit} 
                    ref="tagForm"
                    pending={@state.formPending}
                    disabled={@state.formPending} />
            </div>
        </div>