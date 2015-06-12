"use strict";

import Dispatcher from '../dispatcher';
import {outbox} from '../api/endpoints';
import setToString from '../lib/settostring';
import {token} from './users';

// TODO(vojta) undefined via import from, dont know why, hack for now
const api = require('../api/index.js');

/**
 * Get all
 */
export function getAll() {
  let request = api.get(outbox.index(), { token });

  return Dispatcher.dispatch(getAll, request);
};

/**
 * Delete
 * @param  {String} id
 */
export function remove(id) {
  let request = api.del(outbox.delete(id), { token });

  return Dispatcher.dispatch(remove, request);
};

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('outbox', {
  getAll,
  remove
});
