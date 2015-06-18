"use strict";

import {Record} from 'immutable';

const ContactRecord = Record({
  uuid: null,
  firstName: null,
  lastName: null,
  phoneNumber: null,
  email: null,
  note: null,
  tags: null,
  createdAt: null
});

export default class Contact extends ContactRecord {}