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
        prefix: @refs.prefix.getDOMNode().value
        callbackUrl: @refs.callbackUrl.getDOMNode().value
        note: @refs.note.getDOMNode().value

    render: ->
        <form onSubmit={@props.onSubmit}>
            <div className="line">
                <label>Label</label>
                <input type="text" 
                       name="label" 
                       ref="label" 
                       placeholder="Label" 
                       disabled={@props.disabled}
                       defaultValue={@props.data.label}
                       className="span-3"
                       required />
            </div>
            <div className="line">
                <label>Prefix</label>
                <input type="text" 
                       name="prefix" 
                       ref="prefix" 
                       placeholder="Prefix" 
                       disabled={@props.disabled}
                       defaultValue={@props.data.prefix} />
            </div>
            <div className="line">
                <label>Callback url</label>
                <input type="url" 
                       name="callbackUrl" 
                       ref="callbackUrl" 
                       placeholder="Callback url" 
                       disabled={@props.disabled}
                       defaultValue={@props.data.callbackUrl} />
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