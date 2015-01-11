###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
TemplateForm = require './TemplateForm.coffee'
Subheader = require '../Subheader.coffee'
Dispatcher = require '../../dispatcher.coffee'
TemplateActions = require '../../actions/TemplateActions.coffee'
TemplateStore = require '../../stores/TemplateStore.coffee'


module.exports = React.createClass
    
    mixins: [Router.Navigation]

    getInitialState: ->
        pending: no

    componentDidMount: ->
        TemplateStore.addChangeListener @handleChange
        TemplateStore.addErrorListener @handleError

    handleChange: ->
        @transitionTo '/templates'

    handleError: (err) ->
        console.log err

    handleSubmit: (e) ->
        e.preventDefault()
        console.log 'SUBMIT'
        form = @refs.templateForm
        if form.isValid()
            TemplateActions.add form.getData()

    render: ->
        <div>
            <Subheader back={true} />

            <div id="context">
                <h1>Add form</h1>

                <TemplateForm onSubmit={@handleSubmit} 
                              ref="templateForm"
                              pending={@state.pending}
                              disabled={@state.pending} />
            </div>
        </div>