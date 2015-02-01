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
            <div className="form-group">
                <input type="email" 
                       name="email" 
                       ref="email" 
                       className="form-control"
                       placeholder="E-mail" 
                       required />
            </div>
            <div className="form-group">
                <input type="password" 
                       name="password" 
                       ref="password" 
                       className="form-control"
                       placeholder="Password" 
                       required />
            </div>
            <div className="form-group">
                <input type="text" 
                       name="firstName" 
                       ref="firstName" 
                       className="form-control"
                       placeholder="First name" 
                       required />
            </div>
            <div className="form-group">
                <input type="text" 
                       name="lastName"
                       ref="lastName" 
                       className="form-control"
                       placeholder="Last name" 
                       required />
            </div>
            <div className="form-group">
                <input type="text" 
                       name="company" 
                       ref="company" 
                       className="form-control"
                       placeholder="Company" />
            </div>
            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>Sign up</button>
            </LaddaButton>
        </form>