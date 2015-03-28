###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
UserStore = require '../../stores/UserStore.coffee'
UserActions = require '../../actions/UserActions.coffee'
UserConstants = require '../../constants/UserConstants.coffee'
# components
FlashMessages = require '../components/flash-messages.coffee'
ResetPasswordForm = require './forms/reset-password-form.coffee'
SendEmailForm = require './forms/send-email-form.coffee'


module.exports = React.createClass

    mixins: [Router.Navigation, Router.State]

    getInitialState: ->
        pending: no
        formPending: no
        flashMessages: []
        token: @getParams().token

    componentDidMount: ->
        UserStore.addResponseListener @handleResponse
        UserStore.addErrorListener @handleError

    componentWillUnmount: ->
        UserStore.removeResponseListener @handleResponse
        UserStore.removeErrorListener @handleError

    handleResponse: ({meta, data}) ->
        @setState
            pending: no
            formPending: no
            flashMessages: [ text: meta.message, type: 'success']

        console.log data


    handleError: (err) ->
        @setState
            pending: no
            formPending: no
            flashMessages: [ text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.form
        if form.isValid()
            @setState
                pending: no
                formPending: yes

            UserActions.resetPassword @state.token, form.getData()

    render: ->
        if not @state.token?
            info = """Please fill in your email address and we will send you
                      instructions how to reset your password."""
            form = <SendEmailForm
                    ref="form"
                    onSubmit={@handleSubmit}
                    onError={@handleError}
                    pending={@state.formPending}
                    disabled={@state.formPending} />
        else
            info = "Empty"
            form = <ResetPasswordForm
                    ref="form"
                    onSubmit={@handleSubmit}
                    onError={@handleError}
                    pending={@state.formPending}
                    disabled={@state.formPending} />

        <div id="sign" className="resetPassword">
            <h1><strong>sms</strong>gw</h1>
            <h2>reset password</h2>

            <div className="cleaner"></div>

            <FlashMessages messages={@state.flashMessages} />

            <p>{info}</p>

            {form}

            <div className="info">
                I've remembered my password. <a href="#/sign/in">Sign in</a>.<br />
                Don't have an account? <a href="#/sign/up">Sign up for free</a>.
            </div>
        </div>
