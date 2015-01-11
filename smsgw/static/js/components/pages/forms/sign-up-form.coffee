###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
LaddaButton = require 'react-ladda'

module.exports = React.createClass

    isValid: ->
        yes

    getData: ->
        email: @refs.email.getDOMNode().value
        password: @refs.password.getDOMNode().value
        firstName: @refs.firstName.getDOMNode().value
        lastName: @refs.lastName.getDOMNode().value
        company: @refs.company.getDOMNode().value

    render: ->
        <form onSubmit={@props.onSubmit}>
            <input type="email" name="email" ref="email" placeholder="E-mail" required />
            <input type="password" name="password" ref="password" placeholder="Password" required />
            <input type="text" name="firstName" ref="firstName" placeholder="First name" required />
            <input type="text" name="lastName" ref="lastName" placeholder="Last name" required />
            <input type="text" name="company" ref="company" placeholder="Company" />
            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>Sign up</button>
            </LaddaButton>
        </form>