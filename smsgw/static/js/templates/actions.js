'use strict';

import Dispatcher from '../dispatcher';
import {templates} from '../endpoints';
import setToString from '../lib/settostring';
import {getToken} from '../users/actions';
import * as api from '../api';

/**
 * Get all
 */
export function getAll() {
  const token = getToken();
  const request = api.get(templates.index(), { token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Get specific template
 * @param  {String} uuid
 */
export function get(uuid) {
  const token = getToken();
  const request = api.get(templates.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
}

/**
 * Create new template
 * @param  {Object} data
 */
export function create(data) {
  const token = getToken();
  const request = api.post(templates.create(), { token, data });

  return Dispatcher.dispatch(create, request);
}

/**
 * Update template
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  const token = getToken();
  const request = api.put(templates.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
}

/**
 * Delete template
 * @param  {String} uuid
 */
export function remove(uuid) {
  const token = getToken();
  const request = api.del(templates.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('templates', {
  getAll,
  get,
  create,
  update,
  remove
});
