'use strict';

import Dispatcher from '../dispatcher';
import {phones} from '../endpoints';
import setToString from '../lib/settostring';
import {token} from '../users/actions';
import * as api from '../api';

/**
 * Get all
 */
export function getAll() {
  let request = api.get(phones.index(), { token });

  return Dispatcher.dispatch(getAll, request);
}


// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('sent', {
  getAll
});
