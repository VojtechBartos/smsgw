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
        password: @refs.password.getDOMNode().value

    toggle: ->
        @setState active: !@state.active
        @forceUpdate()

    render: ->
        <form onSubmit={@props.onSubmit}>
            <div className="form-group">
                <input type="email" 
                       name="email" 
                       ref="email" 
                       className="form-control"
                       placeholder="E-mail"
                       disabled={@props.disabled}
                       required />
            </div>
            <div className="form-group">
                <input type="password" 
                       name="password" 
                       ref="password" 
                       className="form-control"
                       placeholder="Password" 
                       disabled={@props.disabled}
                       required />
            </div>
            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>Sign in</button>
            </LaddaButton>
        </form>