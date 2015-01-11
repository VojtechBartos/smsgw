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
SignUpForm = require './forms/sign-up-form.coffee'


module.exports = React.createClass
    
    mixins: [Router.Navigation]

    getInitialState: ->
        pending: no
        flashMessages: []

    componentDidMount: ->
        UserStore.on UserConstants.EVENT.SIGN.UP, @handleResponse

    handleResponse: (data) ->
        messages = []
        if data.success
            @transitionTo '/sign/in'
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
        form = @refs.signUpForm
        if form.isValid()
            @setState pending: yes
            UserActions.signUp form.getData()

    render: ->
        <div id="sign">
            <h1><strong>sms</strong>gw</h1>
            <h2>sign up</h2>

            <div className="cleaner"></div>

            <FlashMessages messages={@state.flashMessages} />

            <SignUpForm 
                ref="signUpForm" 
                onSubmit={@handleSubmit}
                pending={@state.pending}
                disabled={@state.pending} />
            
            <div className="info">
                Have an account already? <a href="#/sign/in">Sign in</a>.
            </div>
        </div>