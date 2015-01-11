###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Dispatcher = require '../../dispatcher.coffee'
UserStore = require '../../stores/UserStore.coffee'
UserActions = require '../../actions/UserActions.coffee'
UserConstants = require '../../constants/UserConstants.coffee'
# components
FlashMessages = require '../components/flash-messages.coffee'
ResetPasswordForm = require './forms/reset-password.coffee'


module.exports = React.createClass

    mixins: [Router.Navigation]

    getInitialState: ->
        pending: no
        flashMessages: []

    componentDidMount: ->
        # UserStore.on UserConstants.EVENT.SIGN.IN, @handleResponse

    handleResponse: (data) ->
        # messages = []
        # if data.success
        #     # save token
        #     UserActions.saveToken data.data.token
        #     # and redirect to dashboard
        #     @transitionTo '/'
        # else
        #     # show flash message
        #     messages.push 
        #         text: data.error.message
        #         type: 'alert'

        # @setState 
        #     pending: no
        #     flashMessages: messages

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.signInForm
        if form.isValid()
            @setState pending: yes

    render: ->
        <div id="sign" className="resetPassword">
            <h1><strong>sms</strong>gw</h1>
            <h2>reset password</h2>

            <div className="cleaner"></div>

            <FlashMessages messages={@state.flashMessages} />

            <p>
                Please fill in your email address and we will send you 
                instructions how to reset your password.
            </p>

            <ResetPasswordForm 
                ref="resetPasswordForm" 
                onSubmit={@handleSubmit} 
                pending={@state.pending}
                disabled={@state.pending} />

            <div className="info">
                I've remembered my password. <a href="#/sign/in">Sign in</a>.<br />
                Don't have an account? <a href="#/sign/up">Sign up for free</a>.
            </div>
        </div>