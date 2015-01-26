###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'

module.exports = React.createClass

    getDefaultProps: ->
        options: []
        items: []
        actions: []

    handleAction: (action, item) ->
        (e) ->
            e.preventDefault()
            action.handler item

    render: ->
        # composite header
        header = []
        for option in @props.options
            header.push <th>{option.label}</th>
        header.push <th>Actions</th>

        # composite items
        items = []
        for item in @props.items
            # fill in basic fileds
            fields = []
            for option in @props.options
                fields.push <td>{item[option.key]}</td>

            # fill in actions
            actions = []
            for action in @props.actions
                onClick = @handleAction action, item
                actions.push <a onClick={onClick}>{action.label}</a>

            fields.push <td>{actions}</td>
            items.push <tr>{fields}</tr>

        <table>
            <tbody>
                <tr>{header}</tr>
                {items}
            </tbody>
        </table>