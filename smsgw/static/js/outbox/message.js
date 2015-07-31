'use strict';

import {Record} from 'immutable';

const MessageRecord = Record({
  id: null,
  application: null,
  contacts: [],
  phoneNumbers: [],
  message: null,
  multiparts: [],
  send: null,
  countOfRespondents: null,
  created: null,
  updated: null
});

export default class Message extends MessageRecord {}
