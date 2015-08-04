'use strict';

import {Record} from 'immutable';
import {server, browser} from '../config';
import moment from 'moment';

const TemplateRecord = Record({
  uuid: null,
  label: null,
  text: null,
  created: null
});

export default class Template extends TemplateRecord {

  get createdDatetime() {
    return moment(moment.utc(this.created, server.datetimeFormat).toDate());
  }

  get createdLocalized() {
    return this.createdDatetime.format(browser.datetimeFormat);
  }

}
