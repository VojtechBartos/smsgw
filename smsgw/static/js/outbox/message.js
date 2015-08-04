'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const MessageRecord = Record({
  id: null,
  application: null,
  contacts: [],
  phoneNumbers: [],
  message: null,
  multiparts: [],
  send: null,
  countOfRespondents: null,
  created: null
});

export default class Message extends MessageRecord {

  get sendDatetime() {
    return moment(moment.utc(this.send, server.datetimeFormat).toDate());
  }

  get sendLocalized() {
    return this.sendDatetime.format(browser.datetimeFormat);
  }

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
