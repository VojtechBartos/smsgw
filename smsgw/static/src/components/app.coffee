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
UserConstants = require '../constants/UserConstants.coffee'

module.exports = React.createClass
   
    mixins: [Router.Navigation]

    getInitialState: ->
        pending: no
        user: 
            firstName: null
            lastName: null
            company: null

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        UserStore.addErrorListener @handleSignOut
        UserActions.fetchMe()
        
        @setState pending: yes

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange
        UserStore.removeErrorListener @handleSignOut

    handleChange: ->
        if @isMounted()
            @setState 
                pending: no
                user: UserStore.me()

    handleSignOut:  ->
        UserActions.token = null
        @transitionTo 'sign-in'

    render: ->
        return <Spinner fullscreen={yes} /> if @state.pending

        <Wrapper>
            <Header firstName={@state.user.firstName} 
                    lastName={@state.user.lastName} 
                    company={@state.user.company} />
            <RouteHandler />
        </Wrapper>