###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
# components
Subheader = require './components/sub-header.coffee'

module.exports = React.createClass
    
    getInitialState: ->
        tags: []
        menu: [
            label: 'Contacts'
            route: 'contacts'
        ,
            label: 'Tags'
            route: 'tags'   
        ]

    render: ->
        <div>
            <Subheader links={@state.menu} />
            <div id="context">
                <h1>
                    Tags ({@state.contacts.length})
                </h1>
            </div>
        </div>