'use strict';

import {Record} from 'immutable';

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

export default class Phone extends PhoneRecord {}
