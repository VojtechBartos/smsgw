###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
UserStore = require '../../stores/UserStore.coffee'
UserActions = require '../../actions/UserActions.coffee'
# components
SignInForm = require './forms/sign-in-form.coffee'
FlashMessages = require '../components/flash-messages.coffee'

module.exports = React.createClass

    mixins: [ Router.Navigation ]

    getInitialState: ->
        formPending: no
        flashMessages: []

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        UserStore.addErrorListener @handleError

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange
        UserStore.removeErrorListener @handleError

    handleChange: (data) ->
        # save token
        UserActions.setToken data.token

        weak = @
        setTimeout ->
            # and redirect to dashboard
            weak.transitionTo 'dashboard'

            if weak.isMounted()
                weak.setState
                    formPending: no
                    flashMessages: []
        , 0

    handleError: (err) ->
        if @isMounted()
            @setState
                formPending: no
                flashMessages: [text: err.message, type: 'danger']

    handleSubmit: (e) ->
        e.preventDefault()
        form = @refs.signInForm
        if form.isValid()
            @setState formPending: yes
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
                pending={@state.formPending}
                disabled={@state.formPending} />

            <div className="info">
                Forgot your password? <Link to="reset-password">Reset Password</Link>.<br />
                Don't have an account? <a href="#/sign/up">Sign up</a> for free.
            </div>
        </div>