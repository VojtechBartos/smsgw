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
        formPending: no
        flashMessages: []

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        UserStore.addErrorListener @handleError

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange
        UserStore.removeErrorListener @handleError

    handleChange: ->
        @transitionTo '/sign/in'

        if @isMounted()
            @setState 
                formPending: no
                flashMessages: []

    handleError: (err) ->
        if @isMounted()
            @setState 
                formPending: no
                flashMessages: [text: err.message, type: 'alert']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.signUpForm
        if form.isValid()
            @setState formPending: yes
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
                pending={@state.formPending}
                disabled={@state.formPending} />
            
            <div className="info">
                Have an account already? <a href="#/sign/in">Sign in</a>.
            </div>
        </div>