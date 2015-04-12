###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
UserStore = require '../../../stores/UserStore.coffee'
UserActions = require '../../../actions/UserActions'
# components
Form = require '../app/forms/settings-form.coffee'
Subheader = require '../app/components/sub-header.coffee'
Spinner = require '../../components/spinner.coffee'
FlashMessages = require '../../components/flash-messages.coffee'


module.exports = React.createClass

    getInitialState: ->
        pending: not UserStore.me()?
        formPending: no
        user: UserStore.me()
        flashMessages: []

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        UserStore.addErrorListener @handleError

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange
        UserStore.removeErrorListener @handleError

    handleChange: ->
        @setState
            pending: no
            user: UserStore.me()

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.settingsForm
        if form.isValid()
            @setState
                pending: yes
                flashMessages: []

            UserActions.update '@me', form.getData()

    handleError: (err) ->
        @setState
            pending: no
            flashMessages: [text: err.message, type: 'danger']

    render: ->
        <div>
            <Subheader>
                <h1>Settings</h1>
                <h2>{@state.user.firstName} {@state.user.lastName}</h2>
            </Subheader>

            <div id="context">
                <FlashMessages messages={@state.flashMessages} />

                <Form
                    onSubmit={@handleSubmit}
                    onError={@handleError}
                    ref="settingsForm"
                    pending={@state.pending}
                    disabled={@state.pending}
                    data={@state.user} />
            </div>
        </div>
