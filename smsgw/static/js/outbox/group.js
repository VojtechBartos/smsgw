'use strict';

import {Record} from 'immutable';

const GroupRecord = Record({
  id: null,
  message: null,
  countOfRespondents: null,
  multiparts: [],
  send: null,
  created: null
});

export default class Group extends GroupRecord {}
