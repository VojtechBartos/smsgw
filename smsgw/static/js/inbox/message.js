'use strict';

import {Record} from 'immutable';

const MessageRecord = Record({
  id: null,
  uuid: null,
  senderNumber: null,
  processed: false,
  application: null,
  contact: null,
  text: null,
  received: null,
  created: null,
  upddate: null
});

export default class Message extends MessageRecord {}
