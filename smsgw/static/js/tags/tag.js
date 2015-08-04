'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const TagRecord = Record({
  uuid: null,
  label: null,
  note: null,
  numberOfContacts: null,
  created: null
});

export default class Tag extends TagRecord {

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
