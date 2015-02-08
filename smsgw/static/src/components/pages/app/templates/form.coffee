###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
# components
Bootstrap = require 'react-bootstrap'
Grid = Bootstrap.Grid
Row = Bootstrap.Row
Col = Bootstrap.Col
Well = Bootstrap.Well
LaddaButton = require 'react-ladda'

module.exports = React.createClass

    getInitialState: ->
        length: 0

    getDefaultProps: ->
        disabled: no
        pending: no
        submitTitle: 'Create'
        data: {}

    isValid: ->
        yes

    getData: ->
        label: @refs.label.getDOMNode().value
        text: @refs.text.getDOMNode().value

    handleTextChange: (e) ->
        @setState length: e.target.value.length

    render: ->
        <form onSubmit={@props.onSubmit}>
            <Grid fluid={yes}>
                <Row>
                    <Col md={4}>
                        <div className="form-group">
                            <label>Label</label>
                            <input type="text"
                                   name="label"
                                   ref="label"
                                   className="form-control"
                                   placeholder="Label"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.label}
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Template body ({@state.length}/160)</label>
                            <textarea name="text"
                                      ref="text"
                                      rows=10
                                      className="form-control"
                                      onChange={@handleTextChange}
                                      disabled={@props.disabled}
                                      defaultValue={@props.data.text}
                                      required></textarea>
                        </div>

                        <LaddaButton
                            active={@props.pending}
                            style="expand-right">
                            <button>{@props.submitTitle}</button>
                        </LaddaButton>
                    </Col>
                    <Col md={2}>
                        <Well bsSize="large" className="margin-top-25">
                            You can use some constant wich will be replaced by
                            real value. We are
                            supporting <strong>{'{firstName}'}</strong>
                             or <strong>{'{lastName}'}</strong> for
                            user first name and last name.
                        </Well>
                    </Col>
                </Row>
            </Grid>
        </form>
