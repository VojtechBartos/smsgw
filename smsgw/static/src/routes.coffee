###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
@cjsx React.DOM
###
"use strict"

# react router
React = require 'react'
Router = require 'react-router'
Route = Router.Route
Routes = Router.Routes
Redirect = Router.Redirect
RouteHandler = Router.RouteHandler
DefaultRoute = Router.DefaultRoute

# pages
App = require './components/app.coffee'
SignIn = require './components/pages/sign-in.coffee'
SignUp = require './components/pages/sign-up.coffee'
ResetPassword = require './components/pages/reset-password.coffee'
Dashboard = require './components/pages/app/dashboard.coffee'
Applications = require './components/pages/app/applications.coffee'
TemplatesList = require './components/pages/app/templates/list.coffee'
TemplatesAdd = require './components/pages/app/templates/add.coffee'
TemplatesEdit = require './components/pages/app/templates/edit.coffee'
Messages = require './components/pages/app/messages.coffee'
Settings = require './components/pages/app/settings.coffee'
Wrapper = require './components/components/wrapper.coffee'
DirectoryWrapper = require './components/pages/app/directory/wrapper.coffee'
ContactsList = require './components/pages/app/directory/contacts/list.coffee'
ContactsAdd = require './components/pages/app/directory/contacts/add.coffee'
ContactsEdit = require './components/pages/app/directory/contacts/edit.coffee'
TagsList = require './components/pages/app/directory/tags/list.coffee'

module.exports =
    <Route handler={Wrapper} path="/">
        <Redirect from="/" to="dashboard" />
        <Redirect from="directory" to="contacts" />
        <Route name="sign-in" path="sign/in" handler={SignIn} />
        <Route name="sign-up" path="sign/up" handler={SignUp} />
        <Route name="reset-password" path="reset-password" handler={ResetPassword} />
        <Route handler={App}>
            <Route name="dashboard" handler={Dashboard} />
            <Route name="applications" handler={Applications} />
            <Route name="messages" handler={Messages} />
            <Route name="directory" handler={Wrapper}>
                <Route handler={DirectoryWrapper}>
                    <Route name="contacts" path="contacts" handler={ContactsList} />
                    <Route name="tags" path="tags" handler={TagsList} />
                </Route>
                <Route name="contact-add" path="contacts/add" handler={ContactsAdd} />
                <Route name="contact-edit" path="contacts/:uuid" handler={ContactsEdit} />
            </Route>
            <Route name="settings" handler={Settings} />
            <Route name="templates" handler={Wrapper}>
                <DefaultRoute handler={TemplatesList} />
                <Route name="template-add" path="add" handler={TemplatesAdd} />
                <Route name="template-edit" path=":uuid" handler={TemplatesEdit} />
            </Route>
        </Route>
    </Route>