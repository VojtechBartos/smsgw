###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

React = require 'react'
Router = require 'react-router'
Routes = require './routes.coffee'


Router
    .create routes: Routes
    .run (Handler) ->
        React.render <Handler />, document.getElementById "smsgw"    