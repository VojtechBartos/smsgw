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
Header = require './Header.coffee'
Spinner = require './helpers/Spinner.coffee'
# stores
UserStore = require '../stores/UserStore.coffee'
UserActions = require '../actions/UserActions.coffee'
UserConstants = require '../constants/UserConstants.coffee'

module.exports = React.createClass
   
    mixins: [Router.Navigation]

    getInitialState: ->
        throbber: yes
        user: 
            firstName: null
            lastName: null
            company: null

    componentDidMount: ->
        UserStore.on UserConstants.EVENT.SIGN.OUT, @handleSignOut
        UserStore.on UserConstants.EVENT.FETCH.ME, @handleFetchMe
        UserActions.fetchMe()

    handleFetchMe: (data) ->
        if data.success and @isMounted()
            @setState 
                throbber: no
                user: data.data
            @forceUpdate()

    handleSignOut: (e) ->
        @transitionTo '/sign/in'

    render: ->
        content = 
            <div>
                <Header firstName={@state.user.firstName} 
                        lastName={@state.user.lastName} 
                        company={@state.user.company} />
                
                <RouteHandler />
            </div>

        if @state.throbber then <Spinner fullscreen /> else content