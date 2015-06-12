###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
UserStore = require '../../../stores/UserStore.coffee'
# components
Wrapper = require '../../components/wrapper'

module.exports = React.createClass

    mixins: [ Router.Navigation ]

    getInitialState: ->
        user: UserStore.me()

    componentDidMount: ->
        UserStore.addChangeListener @handleChange
        @redirectIfIsNotAdmin()

    componentWillUnmount: ->
        UserStore.removeChangeListener @handleChange

    handleChange: ->
        @redirectIfIsNotAdmin()

    redirectIfIsNotAdmin: ->
        if @state.user and @state.user.role != 'admin'
            @transitionTo 'dashboard'

    render: ->
        <Wrapper />
