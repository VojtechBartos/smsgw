###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

_ = require 'lodash'
React = require 'react'
TagStore = require '../../../../../stores/TagStore.coffee'
TagActions = require '../../../../../actions/TagActions'
# components
Bootstrap = require 'react-bootstrap'
Grid = Bootstrap.Grid
Row = Bootstrap.Row
Col = Bootstrap.Col
Label = Bootstrap.Label
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
        tags.push tag.label if _.indexOf(tags, tag.label) == -1

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
                    <Label>{tag}</Label> <a onClick={@handeOnDelete index}>remove</a>
                </li>
            tags.push element

        <form onSubmit={@props.onSubmit}>
            <Grid fluid={yes}>
                <Row>
                    <Col md={3}>
                        <div className="form-group">
                            <label>First name</label>
                            <input type="text"
                                   name="firstName"
                                   ref="firstName"
                                   className="form-control"
                                   placeholder="First name"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.firstName}
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Last name</label>
                            <input type="text"
                                   name="lastName"
                                   ref="lastName"
                                   className="form-control"
                                   placeholder="Last name"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.lastName}
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Phone number</label>
                            <input type="text"
                                   name="phoneNumber"
                                   ref="phoneNumber"
                                   className="form-control"
                                   placeholder="Phone number"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.phoneNumber}
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Email</label>
                            <input type="email"
                                   name="email"
                                   ref="email"
                                   className="form-control"
                                   placeholder="Email"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.email} />
                        </div>
                    </Col>
                    <Col md={3}>
                        <div className="form-group">
                            <label>Note</label>
                            <textarea name="note"
                                      ref="note"
                                      rows=5
                                      className="form-control"
                                      disabled={@props.disabled}
                                      defaultValue={@props.data.note}>
                            </textarea>
                        </div>
                    </Col>
                    <Col md={2}>
                        <div className="form-group">
                            <label>Tags</label>
                            <AutocompleteInput
                                pending={@state.pending.autocomplete}
                                onChange={@handleOnChange}
                                onSelect={@handleOnSelect}
                                options={@state.tags.search} />
                            <div className="cleaner" />
                            <ul>{tags}</ul>
                        </div>

                    </Col>
                </Row>
                <Row>
                    <Col md={3}>
                        <LaddaButton
                            active={@props.pending}
                            style="expand-right">
                            <button>{@props.submitTitle}</button>
                        </LaddaButton>
                    </Col>
                </Row>
            </Grid>
        </form>
