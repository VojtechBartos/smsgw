###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
SignUpForm = require './SignUpForm.coffee'
Dispatcher = require '../../dispatcher.coffee'
UserStore = require '../../stores/UserStore.coffee'
UserActions = require '../../actions/UserActions.coffee'
UserConstants = require '../../constants/UserConstants.coffee'


module.exports = React.createClass
    
    mixins: [Router.Navigation]

    componentDidMount: ->
        UserStore.on UserConstants.EVENT.SIGN.UP, @handleResponse

    handleResponse: (data) ->
        if data.success
            @transitionTo '/sign/in'
        else 
            # TODO(vojta) show message
            console.log data.error

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.signUpForm
        if form.isValid()
            UserActions.signUp form.getData()

    render: ->
        <div id="sign">
            <h1><strong>sms</strong>gw</h1>
            <h2>sign up</h2>

            <div className="cleaner"></div>

            <SignUpForm ref="signUpForm" onSubmit={@handleSubmit}/>
            
            <div className="info">
                Have an account already? <a href="#/sign/in">Sign in</a>.
            </div>
        </div>