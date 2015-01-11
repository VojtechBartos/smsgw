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
Subheader = require '../components/sub-header.coffee'


module.exports = React.createClass
    
    mixins: [Router.Navigation, Router.State]

    getInitialState: ->
        pending: no
        template: TemplateStore.get @getParams().uuid

    componentDidMount: ->
        TemplateStore.addChangeListener @handleChange
        TemplateStore.addErrorListener @handleError

        if @state.template is null
            TemplateActions.get @getParams().uuid

    handleChange: ->
        @setState
            template: TemplateStore.get @getParams().uuid

    handleError: (err) ->
        console.log err

    handleSubmit: (e) ->
        e.preventDefault()
        console.log 'SUBMIT'
        # form = @refs.templateForm
        # if form.isValid()
        #     TemplateActions.add form.getData()

    render: ->
        <div>
            <Subheader back={true} />

            <div id="context">
                <h1>Edit form</h1>

                <TemplateForm onSubmit={@handleSubmit} 
                              ref="templateForm"
                              pending={@state.pending}
                              disabled={@state.pending} />
            </div>
        </div>