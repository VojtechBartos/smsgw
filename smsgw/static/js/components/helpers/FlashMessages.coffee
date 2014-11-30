###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'

module.exports = React.createClass

    render: ->
        messages = []
        if 'messages' of @props
            messages = @props.messages

        <div className="flashes">
            {messages.map (message, index) ->
                <div key={index} className={message.type}>
                    {message.text}
                </div>
            }
        </div>