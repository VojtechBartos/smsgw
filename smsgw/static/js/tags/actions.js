'use strict';

import Dispatcher from '../dispatcher';
import {tags} from '../endpoints';
import setToString from '../lib/settostring';
import {getToken} from '../users/actions';
import * as api from '../api';

/**
 * Search tag by name
 * @param  {String} name
 */
export function search(name) {
  const token = getToken();
  const request = api.get(tags.index(), {
    token,
    query: {
      search: name
    }
  });

  return Dispatcher.dispatch(search, request);
}

/**
 * Get all
 */
export function getAll() {
  const token = getToken();
  const request = api.get(tags.index(), { token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Get specific
 * @param  {String} uuid
 */
export function get(uuid) {
  const token = getToken();
  const request = api.get(tags.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
}

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  const token = getToken();
  const request = api.post(tags.create(), { token, data });

  return Dispatcher.dispatch(create, request);
}

/**
 * Update
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  const token = getToken();
  const request = api.put(tags.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
}

/**
 * Delete
 * @param  {String} uuid
 */
export function remove(uuid) {
  const token = getToken();
  const request = api.del(tags.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('tags', {
  search,
  getAll,
  get,
  create,
  update,
  remove
});
