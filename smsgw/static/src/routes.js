'use strict';

import React from 'react';
import {
  Route,
  Routes,
  Redirect,
  RouteHandler,
  DefaultRoute
} from 'react-router';

// pages
import App from './components/app';
import Wrapper from './components/components/wrapper';
import SignIn from './components/pages/sign-in';
import SignUp from './components/pages/sign-up';
import ResetPassword from './components/pages/reset-password.coffee';
import Dashboard from './components/pages/app/dashboard';
import Messages from './components/pages/app/messages';
import Settings from './components/pages/app/settings';
import AppPages from './components/pages/app';
// messages
import MessagesWrapper from './components/pages/app/messages/wrapper';
import MessagesSent from './components/pages/app/messages/sent';
import MessagesOutbox from './components/pages/app/messages/outbox';
import MessagesCompose from './components/pages/app/messages/compose';
// applications
import ApplicationsList from './components/pages/app/applications/list';
import ApplicationsAdd from './components/pages/app/applications/add';
import ApplicationsShowWrapper from './components/pages/app/applications/wrapper';
import ApplicationsShowSettings from './components/pages/app/applications/show/settings';
import ApplicationsShowOverview from './components/pages/app/applications/show/overview';
import ApplicationsShowSentMessages from './components/pages/app/applications/show/sent-messages';
import ApplicationsShowReceivedMessages from './components/pages/app/applications/show/received-messages';
// templates
import TemplatesList from './components/pages/app/templates/list';
import TemplatesAdd from './components/pages/app/templates/add';
import TemplatesEdit from './components/pages/app/templates/edit';
// contacts
import DirectoryWrapper from './components/pages/app/directory/wrapper';
import ContactsList from './components/pages/app/directory/contacts/list';
import ContactsAdd from './components/pages/app/directory/contacts/add';
import ContactsEdit from './components/pages/app/directory/contacts/edit';
// tags
import TagsList from './components/pages/app/directory/tags/list';
import TagsAdd from './components/pages/app/directory/tags/add';
import TagsEdit from './components/pages/app/directory/tags/edit';
// users
import AdminWrapper from './components/pages/app/admin-wrapper.coffee';
import UsersList from './components/pages/app/users/list';


export default (
  <Route handler={App} path="/">
    <Redirect from="/" to="dashboard" />
    <Redirect from="directory" to="contacts" />
    <Redirect from="messages" to="messages-outbox" />

    <Route name="sign-in" path="sign/in" handler={SignIn} />
    <Route name="sign-up" path="sign/up" handler={SignUp} />
    <Route name="reset-password" path="reset-password/:token?" handler={ResetPassword} />
    <Route handler={AppPages}>
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
