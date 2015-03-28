###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

request = require 'superagent'

# react libs
React = require 'react'
Router = require 'react-router'
RouteHandler = Router.RouteHandler
# components
Header = require './pages/app/components/header.coffee'
Wrapper = require './components/wrapper.coffee'
Spinner = require './components/spinner.coffee'
# stores
UserStore = require '../stores/UserStore.coffee'
UserActions = require '../actions/UserActions.coffee'

module.exports = React.createClass

    mixins: [Router.Navigation]

    getInitialState: ->
        pending: yes
        user: UserStore.me()

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        UserStore.addErrorListener @handleError
        UserActions.fetchMe()

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange
        UserStore.removeErrorListener @handleError

    handleChange: ->
        @setState
            pending: no
            user: UserStore.me()

    handleError: (err) ->
        switch err.status
            when 401
                UserActions.signOut()
                @transitionTo 'sign-in'

            when 403
                @transitionTo 'dashboard'

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <Wrapper>
            <Header user={@state.user} />
            <RouteHandler />
        </Wrapper>
