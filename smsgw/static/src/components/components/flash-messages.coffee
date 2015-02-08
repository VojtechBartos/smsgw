###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
# components
Boostrap = require 'react-bootstrap'
Alert = Boostrap.Alert

module.exports = React.createClass

    getDefaultProps: ->
        messages: []


    render: ->
        <div className="flashes">
            {@props.messages.map (message, index) ->
                <Alert bsStyle={message.type}>
                    {message.text}
                </Alert>
            }
        </div>
