"use strict";

import {Record} from 'immutable';

const ApplicationRecord = Record({
  uuid: null,
  label: null,
  token: null,
  prefix: null,
  callbackUrl: null,
  note: null
});

export default class Application extends ApplicationRecord {}