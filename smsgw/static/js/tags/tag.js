"use strict";

import {Record} from 'immutable';

const TagRecord = Record({
  uuid: null,
  label: null,
  note: null,
  numberOfContacts: null
});

export default class Tag extends TagRecord {}