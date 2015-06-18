"use strict";

import {Record} from 'immutable';

const OutboxRecord = Record({
  id: null,
  destinationNumber: null,
  contact: null,
  text: null,
  send: null,
  created: null,
  upddate: null
});

export default class Outbox extends OutboxRecord {}