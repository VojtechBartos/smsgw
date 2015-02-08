###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'

module.exports = React.createClass

    getDefaultProps: ->
        classNamespace: 'autocomplete'
        pending: no
        options: []
        onChange: null
        onSelect: null

    handleOnChange: (e) ->
        if @props.onChange
            @props.onChange e.target.value

    handleOnSelect: (item) ->
        =>
            @refs.text.getDOMNode().value = ""
            if @props.onSelect
                @props.onSelect item

    render: ->
        options = []
        for option in @props.options
            options.push <li onClick={@handleOnSelect option}>{option.label}</li>
        if options.length > 0
            options = <ul className="options">{options}</ul>
        
        
        throbber = ['throbber']
        throbber.push 'hidden' if not @props.pending

        <div className={@props.classNamespace}>
            <input 
                type="text" 
                ref='text' 
                className="form-control"
                onChange={@handleOnChange} />
            <div className={throbber.join ' '} />
            <div className="cleaner" />
            {options}
        </div>