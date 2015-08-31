'use strict';

import _ from 'lodash';
import * as actions from './actions';
import {usersCursor} from '../state';
import Dispatcher from '../dispatcher';
import User from './user';

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
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      usersCursor(users => {
        return users.withMutations(items => {
          data.forEach(i => {
            const user = items.get(i.uuid);
            if (user && user.isLoggedIn)
              i = _.extend(i, { isLoggedIn: true });

            return items.set(i.uuid, new User(i));
          });
        });
      });
      break;

    case actions.get:
      usersCursor(users => {
        const user = users.get(data.uuid);
        if (user && user.isLoggedIn)
          data = _.extend(data, { isLoggedIn: true });

        return users.set(data.uuid, new User(data));
      });
      break;

    case actions.update:
    case actions.getLoggedIn:
      data = _.extend(data, { isLoggedIn: true });

      usersCursor(users => {
        return users.set(data.uuid, new User(data));
      });
      break;
  }
});
