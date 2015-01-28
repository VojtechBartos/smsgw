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
        style = 
            position: 'relative'
            height: '100%'
            width: '100%'

        content = @props.children
        content = <RouteHandler {...this.props} /> if not content?

        <div style={style}>{content}</div>