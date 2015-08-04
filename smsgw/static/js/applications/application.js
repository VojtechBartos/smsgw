'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const ApplicationRecord = Record({
  uuid: null,
  label: null,
  token: null,
  prefix: null,
  callbackUrl: null,
  note: null,
  created: null
});

export default class Application extends ApplicationRecord {

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
