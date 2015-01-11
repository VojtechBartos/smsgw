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
        pending: no
        disabled: no

    isValid: ->
        yes

    getData: ->
        email: @refs.email.getDOMNode().value

    toggle: ->
        @setState active: !@state.active

    render: ->
        <form onSubmit={@props.onSubmit}>
            <input type="email" 
                   name="email" 
                   ref="email" 
                   placeholder="E-mail"
                   disabled={@props.disabled}
                   required />
            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>Sign in</button>
            </LaddaButton>
        </form>