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
ResetPasswordForm = require './forms/reset-password-form.coffee'


module.exports = React.createClass

    mixins: [Router.Navigation]

    getInitialState: ->
        pending: no
        flashMessages: []

    componentDidMount: ->

    handleResponse: ->
        

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.resetPasswordForm
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