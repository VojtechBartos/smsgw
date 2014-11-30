###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
SignInForm = require './SignInForm.coffee'
Dispatcher = require '../../dispatcher.coffee'
FlashMessages = require '../helpers/FlashMessages.coffee'
UserStore = require '../../stores/UserStore.coffee'
UserActions = require '../../actions/UserActions.coffee'
UserConstants = require '../../constants/UserConstants.coffee'

module.exports = React.createClass

    mixins: [Router.Navigation]

    getInitialState: ->
        pending: no
        flashMessages: []

    componentDidMount: ->
        UserStore.on UserConstants.EVENT.SIGN.IN, @handleResponse

    handleResponse: (data) ->
        messages = []
        if data.success
            # save token
            UserActions.saveToken data.data.token
            # and redirect to dashboard
            @transitionTo '/'
        else
            # show flash message
            messages.push 
                text: data.error.message
                type: 'alert'

        if @isMounted()
            @setState 
                pending: no
                flashMessages: messages

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.signInForm
        if form.isValid()
            @setState pending: yes
            UserActions.signIn form.getData()

    render: ->
        <div id="sign">
            <h1><strong>sms</strong>gw</h1>
            <h2>sign in</h2>

            <div className="cleaner"></div>

            <FlashMessages messages={@state.flashMessages} />

            <SignInForm 
                ref="signInForm" 
                onSubmit={@handleSubmit} 
                pending={@state.pending}
                disabled={@state.pending} />

            <div className="info">
                Forgot your password? <a href="#/sign/reset-password">Reset Password</a>.<br />
                Don't have an account? <a href="#/sign/up">Sign up</a> for free.
            </div>
        </div>