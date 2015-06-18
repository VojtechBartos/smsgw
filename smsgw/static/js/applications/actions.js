"use strict";

import Dispatcher from '../dispatcher';
import {applications} from '../endpoints';
import setToString from '../lib/settostring';
import {token} from '../users/actions';
import * as api from '../api';

/**
 * Get all
 */
export function getAll() {
  let request = api.get(applications.index(), { token });

  return Dispatcher.dispatch(getAll, request);
};

/**
 * Get specific
 * @param  {String} uuid
 */
export function get(uuid) {
  let request = api.get(applications.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
};

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  let request = api.post(applications.create(), { token, data });

  return Dispatcher.dispatch(create, request);
};

/**
 * Update
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let request = api.put(applications.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
};

/**
 * Regenerate token
 * @param {String} uuid
 */
export function regenerateToken(uuid) {
  let request = api.put(applications.regenerate(uuid), { token });

  return Dispatcher.dispatch(regenerateToken, request);
}

/**
 * Delete
 * @param  {String} uuid
 */
export function remove(uuid) {
  let request = api.del(applications.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
};

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('applications', {
  getAll,
  get,
  create,
  update,
  regenerateToken,
  remove
});
