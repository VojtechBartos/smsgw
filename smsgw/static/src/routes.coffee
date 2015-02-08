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
Messages = require './components/pages/app/messages.coffee'
Settings = require './components/pages/app/settings.coffee'
Wrapper = require './components/components/wrapper.coffee'
# messages
MessagesWrapper = require './components/pages/app/messages/wrapper.coffee'
MessagesSent = require './components/pages/app/messages/sent.coffee'
MessagesOutbox = require './components/pages/app/messages/outbox.coffee'
MessagesCompose = require './components/pages/app/messages/compose.coffee'
# applications
ApplicationsList = require './components/pages/app/applications/list.coffee'
ApplicationsAdd = require './components/pages/app/applications/add.coffee'
ApplicationsShowWrapper = require './components/pages/app/applications/wrapper.coffee'
ApplicationsShowSettings = require './components/pages/app/applications/show/settings.coffee'
ApplicationsShowOverview = require './components/pages/app/applications/show/overview.coffee'
ApplicationsShowSentMessages = require './components/pages/app/applications/show/sent-messages.coffee'
ApplicationsShowReceivedMessages = require './components/pages/app/applications/show/received-messages.coffee'
# templates
TemplatesList = require './components/pages/app/templates/list.coffee'
TemplatesAdd = require './components/pages/app/templates/add.coffee'
TemplatesEdit = require './components/pages/app/templates/edit.coffee'
# contacts
DirectoryWrapper = require './components/pages/app/directory/wrapper.coffee'
ContactsList = require './components/pages/app/directory/contacts/list.coffee'
ContactsAdd = require './components/pages/app/directory/contacts/add.coffee'
ContactsEdit = require './components/pages/app/directory/contacts/edit.coffee'
# tags
TagsList = require './components/pages/app/directory/tags/list.coffee'
TagsAdd = require './components/pages/app/directory/tags/add.coffee'
TagsEdit = require './components/pages/app/directory/tags/edit.coffee'
# users
AdminWrapper = require './components/pages/app/admin-wrapper.coffee'
UsersList = require './components/pages/app/users/list.coffee'

module.exports =
    <Route handler={Wrapper} path="/">
        <Redirect from="/" to="dashboard" />
        <Redirect from="directory" to="contacts" />
        <Redirect from="messages" to="messages-outbox" />

        <Route name="sign-in" path="sign/in" handler={SignIn} />
        <Route name="sign-up" path="sign/up" handler={SignUp} />
        <Route name="reset-password" path="reset-password" handler={ResetPassword} />
        <Route handler={App}>
            <Route name="dashboard" handler={Dashboard} />
            <Route name="applications" handler={Wrapper}>
                <DefaultRoute handler={ApplicationsList} />
                <Route name="application-add" path="add" handler={ApplicationsAdd} />
                <Route name="application" path=":uuid" handler={ApplicationsShowWrapper}>
                    <Route name="application-overview" path="overview" handler={ApplicationsShowOverview} />
                    <Route name="application-settings" path="settings" handler={ApplicationsShowSettings} />
                    <Route name="application-sent-messages" path="sent-messages" handler={ApplicationsShowSentMessages} />
                    <Route name="application-received-messages" path="received-messages" handler={ApplicationsShowReceivedMessages} />
                </Route>
            </Route>
            <Route name="messages" handler={MessagesWrapper}>
                <Route name="messages-sent" path="sent" handler={MessagesSent} />
                <Route name="messages-outbox" path="outbox" handler={MessagesOutbox} />
                <Route name="compose" path="compose" handler={MessagesCompose} />
            </Route>
            <Route name="directory" handler={Wrapper}>
                <Route handler={DirectoryWrapper}>
                    <Route name="contacts" path="contacts" handler={ContactsList} />
                    <Route name="tags" path="tags" handler={TagsList} />
                </Route>
                <Route name="contact-add" path="contacts/add" handler={ContactsAdd} />
                <Route name="contact-edit" path="contacts/:uuid" handler={ContactsEdit} />
                <Route name="tag-add" path="tags/add" handler={TagsAdd} />
                <Route name="tag-edit" path="tags/:uuid" handler={TagsEdit} />
            </Route>
            <Route name="settings" handler={Settings} />
            <Route name="templates" handler={Wrapper}>
                <DefaultRoute handler={TemplatesList} />
                <Route name="template-add" path="add" handler={TemplatesAdd} />
                <Route name="template-edit" path=":uuid" handler={TemplatesEdit} />
            </Route>
            <Route name="users" handler={AdminWrapper}>
                <DefaultRoute handler={UsersList} />
            </Route>
        </Route>
    </Route>