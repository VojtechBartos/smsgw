"use strict";

import _ from 'lodash';
import {Record} from 'immutable'
import * as actions from '../actions/users';
import {usersCursor} from '../state';
import Dispatcher from '../dispatcher';

const UserRecord = Record({
  uuid: null,
  email: null,
  firstName: null,
  lastName: null,
  company: null,
  role: null,
  isLoggedIn: false
});

class User extends UserRecord {}


/**
 * Retrieve currently logged in user
 */
export function getLoggedIn() {
  return usersCursor().filter(user => {
    return user.isLoggedIn;
  }).first();
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case actions.getLoggedIn:
      data = _.extend(data, { isLoggedIn: true });

      usersCursor(users => {
        return users.set(data.uuid, new User(data));
      });
      break;

    case actions.update:
      usersCursor(users => {
        return users.set(data.uuid, new User(data));
      });
      break;
  }
});
