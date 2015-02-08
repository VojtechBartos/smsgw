###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

_ = require 'lodash'
React = require 'react'
Boostrap = require 'react-bootstrap'
Label = Boostrap.Label
Table = Boostrap.Table

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
                value = item[option.key]
                content = null
                if _.isBoolean value
                    value = if value then 'yes' else 'no'
                    style = if value then 'success' else 'danger'
                    content = <Label bsStyle={style}>{value}</Label>
                else if _.isArray value
                    content = []
                    for i in value
                        content.push <Label bsStyle="info">{i}</Label>
                else
                    content = value

                fields.push <td key={option.key}>{content}</td>

            # fill in actions
            actions = []
            for action, index in @props.actions
                onClick = @handleAction action, item
                actions.push <a onClick={onClick}>{action.label}</a>
                if index < @props.actions.length - 1
                    actions.push ' | '

            fields.push <td key="actions">{actions}</td>
            items.push <tr>{fields}</tr>

        <Table responsive>
            <thead>
                <tr>
                    {header}
                </tr>
            </thead>
            <tbody>
                {items}
            </tbody>
        </Table>