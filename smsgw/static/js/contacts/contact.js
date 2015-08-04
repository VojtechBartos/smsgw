'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const ContactRecord = Record({
  uuid: null,
  firstName: null,
  lastName: null,
  phoneNumber: null,
  email: null,
  note: null,
  tags: null,
  created: null
});

export default class Contact extends ContactRecord {

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
