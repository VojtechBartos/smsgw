'use strict';

import Dispatcher from '../dispatcher';
import {applications} from '../endpoints';
import setToString from '../lib/settostring';
import {getToken} from '../users/actions';
import * as api from '../api';

/**
 * Get all
 */
export function getAll() {
  const token = getToken();
  const request = api.get(applications.index(), { token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Get specific
 * @param  {String} uuid
 */
export function get(uuid) {
  const token = getToken();
  const request = api.get(applications.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
}

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  const token = getToken();
  const request = api.post(applications.create(), { token, data });

  return Dispatcher.dispatch(create, request);
}

/**
 * Update
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  const token = getToken();
  const request = api.put(applications.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
}

/**
 * Regenerate token
 * @param {String} uuid
 */
export function regenerateToken(uuid) {
  const token = getToken();
  const request = api.put(applications.regenerate(uuid), { token });

  return Dispatcher.dispatch(regenerateToken, request);
}

/**
 * Delete
 * @param  {String} uuid
 */
export function remove(uuid) {
  const token = getToken();
  const request = api.del(applications.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('applications', {
  getAll,
  get,
  create,
  update,
  regenerateToken,
  remove
});
