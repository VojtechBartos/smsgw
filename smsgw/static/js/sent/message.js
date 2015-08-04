'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const SentRecord = Record({
  uuid: null,
  destinationNumber: null,
  contact: null,
  multiparts: 1,
  text: null,
  send: null,
  created: null
});

export default class Sent extends SentRecord {

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
