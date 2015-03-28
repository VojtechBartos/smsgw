import React from 'react'
import {
	Route,
	Routes,
	Redirect,
	RouteHandler,
	DefaultRoute
} from 'react-router'

// pages
import App from './components/app.coffee'
import SignIn from './components/pages/sign-in.coffee'
import SignUp from './components/pages/sign-up.coffee'
import ResetPassword from './components/pages/reset-password.coffee'
import Dashboard from './components/pages/app/dashboard.coffee'
import Messages from './components/pages/app/messages.coffee'
import Settings from './components/pages/app/settings.coffee'
import Wrapper from './components/components/wrapper.coffee'
// messages
import MessagesWrapper from './components/pages/app/messages/wrapper.coffee'
import MessagesSent from './components/pages/app/messages/sent.coffee'
import MessagesOutbox from './components/pages/app/messages/outbox.coffee'
import MessagesCompose from './components/pages/app/messages/compose.coffee'
// applications
import ApplicationsList from './components/pages/app/applications/list.coffee'
import ApplicationsAdd from './components/pages/app/applications/add.coffee'
import ApplicationsShowWrapper from './components/pages/app/applications/wrapper.coffee'
import ApplicationsShowSettings from './components/pages/app/applications/show/settings.coffee'
import ApplicationsShowOverview from './components/pages/app/applications/show/overview.coffee'
import ApplicationsShowSentMessages from './components/pages/app/applications/show/sent-messages.coffee'
import ApplicationsShowReceivedMessages from './components/pages/app/applications/show/received-messages.coffee'
// templates
import TemplatesList from './components/pages/app/templates/list.coffee'
import TemplatesAdd from './components/pages/app/templates/add.coffee'
import TemplatesEdit from './components/pages/app/templates/edit.coffee'
// contacts
import DirectoryWrapper from './components/pages/app/directory/wrapper.coffee'
import ContactsList from './components/pages/app/directory/contacts/list.coffee'
import ContactsAdd from './components/pages/app/directory/contacts/add.coffee'
import ContactsEdit from './components/pages/app/directory/contacts/edit.coffee'
// tags
import TagsList from './components/pages/app/directory/tags/list.coffee'
import TagsAdd from './components/pages/app/directory/tags/add.coffee'
import TagsEdit from './components/pages/app/directory/tags/edit.coffee'
// users
import AdminWrapper from './components/pages/app/admin-wrapper.coffee'
import UsersList from './components/pages/app/users/list.coffee'


export default (
	<Route handler={Wrapper} path="/">
    <Redirect from="/" to="dashboard" />
    <Redirect from="directory" to="contacts" />
    <Redirect from="messages" to="messages-outbox" />

    <Route name="sign-in" path="sign/in" handler={SignIn} />
    <Route name="sign-up" path="sign/up" handler={SignUp} />
    <Route name="reset-password" path="reset-password/:token?" handler={ResetPassword} />
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
)