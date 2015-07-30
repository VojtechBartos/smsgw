'use strict';

import Dispatcher from '../dispatcher';
import {sent} from '../endpoints';
import setToString from '../lib/settostring';
import {getToken} from '../users/actions';
import * as api from '../api';

/**
 * Get all
 */
export function getAll(user = null, application = null) {
  const token = getToken();
  const request = api.get(sent.index(user, application), { token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Delete
 */
export function remove(uuid, application = null, user = '@me') {
  const token = getToken();
  const request = api.del(sent.delete(uuid, application, user), { token });

  return Dispatcher.dispatch(remove, request);
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('sent', {
  getAll,
  remove
});
