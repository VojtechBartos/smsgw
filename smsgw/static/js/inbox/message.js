'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const MessageRecord = Record({
  id: null,
  uuid: null,
  senderNumber: null,
  processed: false,
  application: null,
  contact: null,
  text: null,
  received: null,
  created: null
});

export default class Message extends MessageRecord {

  get receivedDatetime() {
    return moment(moment.utc(this.received, server.datetimeFormat).toDate());
  }

  get receivedLocalized() {
    return this.receivedDatetime.format(browser.datetimeFormat);
  }

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
