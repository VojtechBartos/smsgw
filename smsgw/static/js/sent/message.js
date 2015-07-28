'use strict';

import {Record} from 'immutable';

const SentRecord = Record({
  id: null,
  destinationNumber: null,
  contact: null,
  text: null,
  send: null,
  created: null,
  upddate: null
});

export default class Sent extends SentRecord {}
