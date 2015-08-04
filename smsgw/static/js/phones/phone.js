'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const PhoneRecord = Record({
  id: null,
  uuid: null,
  hostname: null,
  imei: null,
  netCode: null,
  netName: null,
  battery: null,
  signal: null,
  client: null,
  sent: null,
  received: null,
  sendEnabled: null,
  receiveEnabled: null,
  lastActivity: null,
  created: null,
  updated: null
});

export default class Phone extends PhoneRecord {

  get lastActivityDatetime() {
    return moment(moment.utc(this.lastActivity, server.datetimeFormat).toDate());
  }

  get lastActivityLocalized() {
    return this.lastActivityDatetime.format(browser.datetimeFormat);
  }

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
