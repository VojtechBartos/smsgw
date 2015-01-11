###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
RouteHandler = Router.RouteHandler

module.exports = React.createClass
    render: ->
        <RouteHandler />