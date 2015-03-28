###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
ContactActions = require '../../../../../actions/ContactActions.coffee'
ContactStore = require '../../../../../stores/ContactStore.coffee'
# components
ContactForm = require './form.coffee'
FlashMessages = require '../../../../components/flash-messages.coffee'
Subheader = require '../../components/sub-header.coffee'
Spinner = require '../../../../components/spinner.coffee'

module.exports = React.createClass

    mixins: [Router.Navigation, Router.State]

    getInitialState: ->
        pending: no
        formPending: no
        flashMessages: []
        contact:
            firstName: null
            lastName: null
            phoneNumber: null

    componentDidMount: ->
        ContactStore.addChangeListener @handleChange
        ContactStore.addErrorListener @handleError

        ContactActions.fetch @getParams().uuid
        @setState pending: yes

    componentWillUnmount: ->
        ContactStore.removeChangeListener @handleChange
        ContactStore.removeErrorListener @handleError

    handleChange: (data) ->
        if @isMounted()
            @setState
                pending: no
                formPending: no
                contact: ContactStore.get @getParams().uuid
                flashMessages: []

    handleError: (err) ->
        if @isMounted()
            @setState
                pending: no
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.contactForm
        if form.isValid()
            @setState formPending: yes
            ContactActions.update @state.contact.uuid, form.getData()

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <div>
            <Subheader backTitle="Contacts">
                <h1>{@state.contact.firstName} {@state.contact.lastName}</h1>
                <h2>{@state.contact.phoneNumber}</h2>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <ContactForm
                    onSubmit={@handleSubmit}
                    ref="contactForm"
                    pending={@state.formPending}
                    disabled={@state.formPending}
                    submitTitle="Edit"
                    data={@state.contact} />
            </div>
        </div>