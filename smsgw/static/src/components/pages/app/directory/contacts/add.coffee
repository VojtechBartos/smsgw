###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Dispatcher = require '../../../../../dispatcher.coffee'
ContactActions = require '../../../../../actions/ContactActions.coffee'
ContactStore = require '../../../../../stores/ContactStore.coffee'
# components
ContactForm = require './form.coffee'
FlashMessages = require '../../../../components/flash-messages.coffee'
Subheader = require '../../components/sub-header.coffee'

module.exports = React.createClass
    
    mixins: [ Router.Navigation ]

    getInitialState: ->
        formPending: no
        flashMessages: []

    componentDidMount: ->
        ContactStore.addChangeListener @handleChange
        ContactStore.addErrorListener @handleError

    componentWillUnmount: ->
        ContactStore.removeChangeListener @handleChange
        ContactStore.removeErrorListener @handleError

    handleChange: ->
        @transitionTo 'contacts'

    handleError: (err) ->
        if @isMounted()
            @setState
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.contactForm
        if form.isValid()
            @setState formPending: yes
            ContactActions.create form.getData()

    render: ->
        <div>
            <Subheader backTitle="Contacts">
                <h1>Add contact</h1>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <ContactForm 
                    onSubmit={@handleSubmit} 
                    ref="contactForm"
                    pending={@state.formPending}
                    disabled={@state.formPending} />
            </div>
        </div>