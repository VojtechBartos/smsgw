###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
# components
LaddaButton = require 'react-ladda'
{Grid, Row, Col} = require 'react-bootstrap'

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
            <Grid fluid={yes}>
                <Row>
                    <Col md={4}>
                        <div className="form-group">
                            <label>Label</label>
                            <input type="text"
                                   name="label"
                                   ref="label"
                                   placeholder="Label"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.label}
                                   className="form-control"
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Prefix</label>
                            <input type="text"
                                   name="prefix"
                                   ref="prefix"
                                   placeholder="Prefix"
                                   className="form-control"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.prefix} />
                        </div>
                        <div className="form-group">
                            <label>Callback url</label>
                            <input type="url"
                                   name="callbackUrl"
                                   ref="callbackUrl"
                                   placeholder="Callback url"
                                   className="form-control"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.callbackUrl} />
                        </div>
                        <div className="form-group">
                            <label>Note</label>
                            <textarea name="note"
                                      ref="note"
                                      disabled={@props.disabled}
                                      defaultValue={@props.data.note}
                                      className="form-control"
                                      rows=10></textarea>
                        </div>

                        <div className="cleaner" />

                        <LaddaButton
                            active={@props.pending}
                            style="expand-right">
                            <button>{@props.submitTitle}</button>
                        </LaddaButton>
                    </Col>
                </Row>
            </Grid>
        </form>
