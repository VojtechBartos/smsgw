###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

# react libs
React = require 'react'
Router = require 'react-router'
Route = Router.Route
Routes = Router.Routes
Redirect = Router.Redirect
RouteHandler = Router.RouteHandler
DefaultRoute = Router.DefaultRoute
# components
SmsgwApp = require './components/SmsgwApp.coffee'
Sign = require './components/sign/Sign.coffee'
SignIn = require './components/sign/SignIn.coffee'
SignUp = require './components/sign/SignUp.coffee'
ResetPassword = require './components/sign/ResetPassword.coffee'
Dashboard = require './components/Dashboard.coffee'
Applications = require './components/Apps.coffee'
Templates = require './components/Templates.coffee'
Messages = require './components/Messages.coffee'
Contacts = require './components/Contacts.coffee'



App = React.createClass
    render: ->
        <RouteHandler />

routes =
    <Route handler={App} path="/">
        <DefaultRoute handler={Dashboard}/>
        <Route path="/sign" handler={Sign}>
            <Route name="sign-in" path="in" handler={SignIn} />
            <Route name="sign-up" path="up" handler={SignUp} />
            <Route name="reset-password" path="reset-password" handler={ResetPassword} />
        </Route>
        <Route handler={SmsgwApp}>
            <Route name="dashboard" handler={Dashboard} />
            <Route name="applications" handler={Applications} />
            <Route name="templates" handler={Templates} />
            <Route name="messages" handler={Messages} />
            <Route name="contacts" handler={Contacts} />
        </Route>
    </Route>

Router.run routes, (Handler) ->
    React.render <Handler />, document.getElementById "smsgw"
