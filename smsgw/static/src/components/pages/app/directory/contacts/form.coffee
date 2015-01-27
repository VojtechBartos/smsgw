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
        firstName: @refs.firstName.getDOMNode().value
        lastName: @refs.lastName.getDOMNode().value
        phoneNumber: @refs.phoneNumber.getDOMNode().value
        email: @refs.email.getDOMNode().value
        note: @refs.note.getDOMNode().value

    render: ->
        <form onSubmit={@props.onSubmit}>
            <div className="line">
                <label>First name</label>
                <input type="text" 
                       name="firstName" 
                       ref="firstName" 
                       placeholder="First name" 
                       disabled={@props.disabled}
                       defaultValue={@props.data.firstName}
                       className="span-3"
                       required />
            </div>
            <div className="line">
                <label>Last name</label>
                <input type="text" 
                       name="lastName" 
                       ref="lastName" 
                       placeholder="Last name" 
                       disabled={@props.disabled}
                       defaultValue={@props.data.lastName}
                       className="span-3"
                       required />
            </div>
            <div className="line">
                <label>Phone number</label>
                <input type="text" 
                       name="phoneNumber" 
                       ref="phoneNumber" 
                       placeholder="Phone number" 
                       disabled={@props.disabled}
                       defaultValue={@props.data.phoneNumber}
                       className="span-4"
                       required />
            </div>
            <div className="line">
                <label>Email</label>
                <input type="email" 
                       name="email" 
                       ref="email" 
                       placeholder="E-mail" 
                       disabled={@props.disabled}
                       className="span-3"
                       defaultValue={@props.data.email} />
            </div>
            <div className="line">
                <label>Note</label>
                <textarea name="note" 
                          ref="note" 
                          disabled={@props.disabled} 
                          defaultValue={@props.data.note}
                          className="span-3"
                          rows=10></textarea>
            </div>

            <div className="cleaner" />

            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>{@props.submitTitle}</button>
            </LaddaButton>
        </form>