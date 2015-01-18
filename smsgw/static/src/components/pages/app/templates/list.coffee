###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Link = Router.Link
TemplateConstants = require '../../../../constants/TemplateConstants.coffee'
TemplateActions = require '../../../../actions/TemplateActions.coffee'
TemplateStore = require '../../../../stores/TemplateStore.coffee'
# components
Subheader = require './../components/sub-header.coffee'


TemplateTableHeader = React.createClass

    render: ->
        <tr>
            <td>Label</td>
            <td>Content</td>
            <td>Created at</td>
        </tr>


TemplateTableItem = React.createClass

    getDefaultProps: ->
        uuid: null,
        label: null,
        text: "",
        createdAt: null

    handleDelete: (e) ->
        e.preventDefault()
        TemplateActions.delete(@props.uuid)

    render: ->
        <tr>
            <td>{@props.label}</td>
            <td>{@props.text}</td>
            <td>{@props.createdAt}</td>
            <td>
                <Link to="template-edit" params={{uuid: @props.uuid}}>Edit</Link>
                <a href="#" onClick={@handleDelete}>Delete</a>
            </td>
        </tr>


Templates = React.createClass
      
    getInitialState: ->
        templates: TemplateStore.getAll()

    componentDidMount: ->
        TemplateStore.addChangeListener @handleResponse
        TemplateActions.fetchAll()

    handleResponse: (data) ->
        if @isMounted()
            @setState
                templates: TemplateStore.getAll()

    render: ->
        menu = [
            route: 'template-add'
            label: 'Add template'
        ]

        items = []
        for template in @state.templates
            items.push <TemplateTableItem uuid={template.uuid} 
                                          label={template.label} 
                                          text={template.text} 
                                          createdAt={template.createdAt} />
        

        <div>
            <Subheader links={menu} />

            <div id="context">
                <h1>Templates</h1>
                <table>
                    <TemplateTableHeader />
                    {items}
                </table>
            </div>
        </div>

module.exports = Templates