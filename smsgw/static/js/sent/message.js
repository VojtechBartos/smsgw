'use strict';

import {Record} from 'immutable';

const SentRecord = Record({
  uuid: null,
  destinationNumber: null,
  contact: null,
  multiparts: 1,
  text: null,
  send: null,
  created: null
});

export default class Sent extends SentRecord {}
