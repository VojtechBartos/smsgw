###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'

Dashboard = React.createClass
    mixins : [ Router.Navigation ]
    render: ->
        <div onClick={@handleClick}>Dashboard</div>

    handleClick: ->
        @transitionTo '/sign/in'


module.exports = Dashboard