'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const UserRecord = Record({
  uuid: null,
  email: null,
  firstName: null,
  lastName: null,
  company: null,
  role: null,
  isLoggedIn: false,
  isActive: false,
  numbers: {
    contacts: 0,
    sent: 0,
    tags: 0,
    outbox: 0,
    inbox: 0,
    templates: 0,
    applications: 0
  },
  created: null
});

export default class User extends UserRecord {

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
