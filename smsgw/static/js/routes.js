'use strict';

import React from 'react';
import { Route, Redirect, DefaultRoute } from 'react-router';

// pages
import Wrapper from './components/wrapper.react';
import Main from './app/main.react';
import Signin from './users/signin.react';
import Signup from './users/signup.react';
import App from './app/app.react';
import Dashboard from './pages/dashboard.react';
import Settings from './pages/settings.react';
import Directory from './pages/directory.react';
// templates
import Templates from './templates/list.react';
import TemplatesAdd from './templates/add.react';
import TemplatesEdit from './templates/edit.react';
// contacts
import Contacts from './contacts/list.react';
import ContactsAdd from './contacts/add.react';
import ContactsEdit from './contacts/edit.react';
// tags
import Tags from './tags/list.react';
import TagsAdd from './tags/add.react';
import TagsEdit from './tags/edit.react';
// messages
import Messages from './pages/messages.react';
import Sent from './sent/list.react';
import Outbox from './outbox/list.react';
import Compose from './outbox/compose.react';
import Inbox from './inbox/list.react';
// applications
import Applications from './applications/list.react';
import ApplicationsAdd from './applications/add.react';
import ApplicationsWrapper from './applications/wrapper.react';
import ApplicationsSettings from './applications/settings.react';
import ApplicationsOverview from './applications/overview.react';
// admin
import Admin from './pages/admin.react';
import Users from './users/list.react';
import Phones from './phones/list.react';
import PhonesDetail from './phones/detail.react';
import InboxNoResolved from './pages/inbox.react';


export default (
  <Route handler={Main} path="/">
    <Redirect from="/" to="dashboard" />
    <Redirect from="directory" to="contacts" />
    <Redirect from="messages" to="messages-outbox" />

    <Route name="signin" path="sign/in" handler={Signin} />
    <Route name="signup" path="sign/up" handler={Signup} />

    <Route handler={App}>
      <Route name="dashboard" handler={Dashboard} />

      <Route name="applications" handler={Wrapper}>
        <DefaultRoute handler={Applications} />
        <Route name="application-add" path="add" handler={ApplicationsAdd} />
        <Route name="application" path=":uuid" handler={ApplicationsWrapper}>
          <Route name="application-overview" path="overview" handler={ApplicationsOverview} />
          <Route name="application-settings" path="settings" handler={ApplicationsSettings} />
          <Route name="application-outbox" path="outbox" handler={Outbox} />
          <Route name="application-sent-messages" path="sent" handler={Sent} />
          <Route name="application-received-messages" path="received" handler={Inbox} />
          </Route>
      </Route>

      <Route name="messages" handler={Messages}>
        <Route name="messages-sent" path="sent" handler={Sent} />
        <Route name="messages-outbox" path="outbox" handler={Outbox} />
        <Route name="compose" path="compose" handler={Compose} />
      </Route>

      <Route name="templates" handler={Wrapper}>
        <DefaultRoute handler={Templates} />
        <Route name="template-add" path="add" handler={TemplatesAdd} />
        <Route name="template-edit" path=":uuid" handler={TemplatesEdit} />
      </Route>

      <Route name="directory" handler={Wrapper}>
        <Route handler={Directory}>
          <Route name="contacts" path="contacts" handler={Contacts} />
          <Route name="tags" path="tags" handler={Tags} />
        </Route>
        <Route name="contact-add" path="contacts/add" handler={ContactsAdd} />
        <Route name="contact-edit" path="contacts/:uuid" handler={ContactsEdit} />
        <Route name="tag-add" path="tags/add" handler={TagsAdd} />
        <Route name="tag-edit" path="tags/:uuid" handler={TagsEdit} />
      </Route>

      <Route name="settings" handler={Settings} />

      <Route handler={Admin}>
        <Route name="users" handler={Wrapper}>
          <DefaultRoute handler={Users} />
        </Route>
        <Route name="phones" handler={Wrapper}>
          <DefaultRoute handler={Phones} />
          <Route name="phone-detail" path=":uuid/" handler={PhonesDetail} />
        </Route>
        <Route name="inbox" handler={InboxNoResolved} />
      </Route>
    </Route>
  </Route>
);
