###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

# react libs
React = require 'react'
Router = require 'react-router'
RouteHandler = Router.RouteHandler

# components
Sign = React.createClass
    render: ->
        <RouteHandler />

module.exports = Sign