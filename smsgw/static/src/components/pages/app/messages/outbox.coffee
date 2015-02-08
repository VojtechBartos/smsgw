###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
moment = require 'moment'
OutboxActions = require '../../../../actions/OutboxActions.coffee'
OutboxStore = require '../../../../stores/OutboxStore.coffee'
# components
Link = Router.Link
Subheader = require './../components/sub-header.coffee'
Table = require './../components/table.coffee'
Spinner = require '../../../components/spinner.coffee'
Bootstrap = require 'react-bootstrap'
{Table, DropdownButton, MenuItem} = require 'react-bootstrap'

module.exports = React.createClass
      
    mixins: [ Router.Navigation ]

    getInitialState: ->
        pending: no
        messages: []

    componentDidMount: ->
        OutboxStore.addChangeListener @handleChange
        OutboxActions.fetchAll()

        @setState pending: yes

    componentWillUnmount: ->
        OutboxStore.removeChangeListener @handleChange

    handleChange: ->
        state = 
            pending: no
            messages: OutboxStore.getAll 'send'
        
        @setState state, ->
            setTimeout ->
                OutboxActions.fetchAll()
            , 30000      

    handleDelete: (message) ->
        (e) =>
            e.preventDefault()
            @setState pending: yes
            OutboxActions.delete message.id
            
    render: ->
        self = @
        return <Spinner fullscreen={yes} /> if @state.pending

        <div id="context">
            <h1>Outbox ({@state.messages.length})</h1>

            <Table>
                <thead>
                    <tr>
                        <th>To</th>
                        <th>Text</th>
                        <th>Sending at</th>
                        <th>Created</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    {@state.messages.map (message, i) ->
                        contact = ->
                            if not message.contact?
                                return message.destinationNumber
                            
                            <Link to="contact-edit" 
                                  params={uuid: message.contact.uuid}>
                                {message.contact.lastName} {message.contact.firstName}
                            </Link>

                        send = ->
                            return if not message.send?
                            dt = moment message.send
                            "#{dt.format 'HH:mm DD.MM.YYYY'} (#{dt.from moment()})"

                        <tr key={i}>
                            <td>{contact()}</td>
                            <td>{message.text}</td>
                            <td>{send()}</td>
                            <td>{moment(message.created).format 'HH:mm DD.MM.YYYY'}</td>
                            <td>
                                <DropdownButton 
                                    title="actions" 
                                    bsStyle="primary" 
                                    bsSize="xsmall">
                                    <MenuItem eventKey="1">Edit</MenuItem>
                                    <MenuItem 
                                        eventKey="2" 
                                        onClick={self.handleDelete message}>
                                        Delete
                                    </MenuItem>
                                </DropdownButton>
                            </td>
                        </tr>
                    }
                </tbody>
            </Table>
        </div>