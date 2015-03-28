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
        onSubmit: null
        onError: null

    isValid: ->
        valid = yes
        password = @refs.password.getDOMNode().value
        passwordVerify = @refs.passwordVerify.getDOMNode().value

        if password or password.length > 0
            if password != passwordVerify
                valid = no
                msg = "Password and verify password needs to be same"
                @props.onError message: msg if @props.onError
        valid

    getData: ->
        password: @refs.password.getDOMNode().value

    render: ->
        <form onSubmit={@props.onSubmit}>
            <div className="form-group">
                <input type="password"
                       name="password"
                       ref="password"
                       className="form-control"
                       placeholder="Password"
                       disabled={@props.disabled}
                       required />
            </div>
            <div className="form-group">
                <input type="password"
                       name="passwordVerify"
                       ref="passwordVerify"
                       className="form-control"
                       placeholder="Verfiy password"
                       disabled={@props.disabled}
                       required />
            </div>
            <LaddaButton
                active={@props.pending}
                style="expand-right">
                <button>Save password</button>
            </LaddaButton>
        </form>
