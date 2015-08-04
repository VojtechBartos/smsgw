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
