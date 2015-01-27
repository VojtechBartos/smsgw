###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

_ = require 'lodash'
React = require 'react'
TagStore = require '../../../../../stores/TagStore.coffee'
TagActions = require '../../../../../actions/TagActions.coffee'
# components
AutocompleteInput = require '../../../../components/autocomplete-input.coffee'
LaddaButton = require 'react-ladda'


module.exports = React.createClass

    getInitialState: ->
        tags: 
            selected: @props.data.tags or []
            search: [] 
        pending:
            autocomplete: no

    getDefaultProps: ->
        disabled: no
        pending: no
        submitTitle: 'Create'
        data: {}

    componentDidMount: ->
        TagStore.addChangeListener @handleStoreChange

    componentWillUnmount: ->
        TagStore.removeChangeListener @handleStoreChange

    handleStoreChange: ->
        @setState 
            pending:
                autocomplete: no
            tags:
                selected: @state.tags.selected
                search: TagStore.getAll()

    handleOnChange: (value) ->
        @setState pending: autocomplete: yes
        TagActions.search value

    handleOnSelect: (tag) ->
        tags = @state.tags.selected
        tags.push tag.label if not _.some tags, tag.label
            
        @setState 
            tags: 
                selected: tags
                search: []

    handeOnDelete: (index) ->
        =>
            tags = @state.tags.selected
            tags.splice index, 1
            @setState tags: selected: tags

    isValid: ->
        yes

    getData: ->
        firstName: @refs.firstName.getDOMNode().value
        lastName: @refs.lastName.getDOMNode().value
        phoneNumber: @refs.phoneNumber.getDOMNode().value
        email: @refs.email.getDOMNode().value
        note: @refs.note.getDOMNode().value
        tags: @state.tags.selected || []

    render: ->
        # create items for tags
        tags = []
        for tag, index in @state.tags.selected
            element =
                <li>
                    {tag} <a onClick={@handeOnDelete index}>remove</a>
                </li>
            tags.push element
        
        <form onSubmit={@props.onSubmit}>
            <div className="line">
                <div className="left span-3">
                    <div className="line">
                        <label>First name</label>
                        <input type="text" 
                               name="firstName" 
                               ref="firstName" 
                               placeholder="First name" 
                               disabled={@props.disabled}
                               defaultValue={@props.data.firstName}
                               className="span-1"
                               required />
                        <div className="cleaner" />
                    </div>
                    <div className="line">
                        <label>Last name</label>
                        <input type="text" 
                               name="lastName" 
                               ref="lastName" 
                               placeholder="Last name" 
                               disabled={@props.disabled}
                               defaultValue={@props.data.lastName}
                               className="span-1"
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
                               className="span-1"
                               defaultValue={@props.data.email} />
                    </div>
                    <div className="line">
                        <label>Note</label>
                        <textarea name="note" 
                                  ref="note" 
                                  disabled={@props.disabled} 
                                  defaultValue={@props.data.note}
                                  className="span-1"
                                  rows=10></textarea>
                    </div>

                    <div className="cleaner" />
                </div>

                <div className="tags">
                    <label>Tags</label>
                    <AutocompleteInput
                        pending={@state.pending.autocomplete} 
                        onChange={@handleOnChange} 
                        onSelect={@handleOnSelect}
                        options={@state.tags.search} />
                    <div className="cleaner" />
                    <ul>{tags}</ul>
                </div>
            </div>

            <div className="cleaner" />

            <LaddaButton 
                active={@props.pending}
                style="expand-right">
                <button>{@props.submitTitle}</button>
            </LaddaButton>
        </form>