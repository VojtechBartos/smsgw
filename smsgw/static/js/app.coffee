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
# components
SmsgwApp = require './components/SmsgwApp.coffee'
Sign = require './components/sign/Sign.coffee'
SignIn = require './components/sign/SignIn.coffee'
SignUp = require './components/sign/SignUp.coffee'
Dashboard = require './components/Dashboard.coffee'
Applications = require './components/Apps.coffee'
Templates = require './components/Templates.coffee'
Messages = require './components/Messages.coffee'
Contacts = require './components/Contacts.coffee'

routes =
    <Routes>
        <Route path="/sign" handler={Sign}>
            <Route name="sign-in" path="in" handler={SignIn} />
            <Route name="sign-up" path="up" handler={SignUp} />
        </Route>
        <Route handler={SmsgwApp}>
            <Route name="dashboard" path="/" handler={Dashboard} />
            <Route name="applications" handler={Applications} />
            <Route name="templates" handler={Templates} />
            <Route name="messages" handler={Messages} />
            <Route name="contacts" handler={Contacts} />
        </Route>
    </Routes>

React.renderComponent routes, document.getElementById "smsgw"