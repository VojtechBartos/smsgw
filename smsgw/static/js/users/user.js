"use strict";

import {Record} from 'immutable';

const UserRecord = Record({
  uuid: null,
  email: null,
  firstName: null,
  lastName: null,
  company: null,
  role: null,
  isLoggedIn: false
});

export default class User extends UserRecord {}