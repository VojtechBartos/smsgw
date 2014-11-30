###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
UserActions = require '../actions/UserActions.coffee'
UserStore = require '../stores/UserStore.coffee'


Templates = React.createClass
      
    compononentDidMount: ->
        UserStore.on 'change', @handleChange

    handleClick: ->
        UserActions.fetchMe()

    handleChange: (e) ->
        console.log 'RECEVICED'
        console.log e

    render: ->
        <div onClick={@handleClick}>Templates</div>

module.exports = Templates