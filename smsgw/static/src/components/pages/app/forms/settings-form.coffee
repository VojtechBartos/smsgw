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
        data: {}
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
        password = @refs.password.getDOMNode().value

        firstName: @refs.firstName.getDOMNode().value
        lastName: @refs.lastName.getDOMNode().value
        email: @refs.email.getDOMNode().value
        company: @refs.company.getDOMNode().value
        password: if password.length == 0 then null else password

    render: ->
        <form onSubmit={@props.onSubmit}>
            <Grid fluid={yes}>
                <Row>
                    <Col md={4}>
                        <div className="form-group">
                            <label>E-Mail</label>
                            <input type="email"
                                   name="email"
                                   ref="email"
                                   placeholder="E-mail"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.email}
                                   className="form-control"
                                   required />
                        </div>
                        <div className="form-group">
                            <label>First name</label>
                            <input type="text"
                                   name="firstName"
                                   ref="firstName"
                                   placeholder="First name"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.firstName}
                                   className="form-control"
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Last name</label>
                            <input type="text"
                                   name="lastName"
                                   ref="lastName"
                                   placeholder="Last name"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.lastName}
                                   className="form-control"
                                   required />
                        </div>
                        <div className="form-group">
                            <label>Company</label>
                            <input type="text"
                                   name="company"
                                   ref="company"
                                   placeholder="Comapny"
                                   disabled={@props.disabled}
                                   defaultValue={@props.data.company}
                                   className="form-control" />
                        </div>

                        <div className="form-group">
                            <label>Password</label>
                            <input type="password"
                                   name="password"
                                   ref="password"
                                   placeholder="Password"
                                   disabled={@props.disabled}
                                   className="form-control" />
                        </div>
                        <div className="form-group">
                            <label>Verify password</label>
                            <input type="password"
                                   name="passwordVerify"
                                   ref="passwordVerify"
                                   placeholder="Verify password"
                                   disabled={@props.disabled}
                                   className="form-control" />
                        </div>

                        <div className="cleaner" />

                        <LaddaButton
                            active={@props.pending}
                            style="expand-right">
                            <button>Save</button>
                        </LaddaButton>
                    </Col>
                </Row>
            </Grid>
        </form>
