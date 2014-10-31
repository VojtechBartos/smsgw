###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

request = require 'superagent'

# react libs
React = require 'react'
# components
Header = require './Header.coffee'
SmsgwApp = React.createClass

    componentDidMount: ->
        console.log 'DID mount'

    componentWillMount: ->
        request
            .get '/api/1.0/users'
            .type 'application/json'
            .end (res) ->
                console.log 'DONE'
                console.log res

    render: ->
        <div>
            <Header />
            <div id="subheader">
                Test
            </div>
            {@props.activeRouteHandler()}
        </div>

module.exports = SmsgwApp
