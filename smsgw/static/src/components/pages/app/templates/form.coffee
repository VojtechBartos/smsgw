###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
LaddaButton = require 'react-ladda'

module.exports = React.createClass

    getDefaultProps: ->
        disabled: no
        pending: no
        submitTitle: 'Create'
        data: {}

    isValid: ->
        yes

    getData: ->
        label: @refs.label.getDOMNode().value
        text: @refs.text.getDOMNode().value

    render: ->
        <form onSubmit={@props.onSubmit}>
            <input type="text" 
                   name="label" 
                   ref="label" 
                   placeholder="Label" 
                   disabled={@props.disabled}
                   defaultValue={@props.data.label}
                   required />
            <textarea name="text" 
                      ref="text" 
                      disabled={@props.disabled} 
                      defaultValue={@props.data.text}
                      required></textarea>
            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>{@props.submitTitle}</button>
            </LaddaButton>
        </form>