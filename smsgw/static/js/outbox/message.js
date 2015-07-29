'use strict';

import {Record} from 'immutable';

const OutboxRecord = Record({
  id: null,
  uuid: null,
  destinationNumber: null,
  contact: null,
  multiparts: [],
  text: null,
  send: null,
  created: null,
  upddate: null
});

export default class Outbox extends OutboxRecord {}
