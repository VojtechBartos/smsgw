"use strict";

import Dispatcher from '../dispatcher';
import {tags} from '../endpoints';
import setToString from '../lib/settostring';
import {token} from '../users/actions';
import * as api from '../api';

/**
 * Search tag by name
 * @param  {String} name
 */
export function search(name) {
  let request = api.get(tags.index(), {
    token,
    query: {
      search: name
    }
  });

  return Dispatcher.dispatch(search, request);
};

/**
 * Get all
 */
export function getAll() {
  let request = api.get(tags.index(), { token });

  return Dispatcher.dispatch(getAll, request);
};

/**
 * Get specific
 * @param  {String} uuid
 */
export function get(uuid) {
  let request = api.get(tags.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
};

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  let request = api.post(tags.create(), { token, data });

  return Dispatcher.dispatch(create, request);
};

/**
 * Update
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let request = api.put(tags.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
};

/**
 * Delete
 * @param  {String} uuid
 */
export function remove(uuid) {
  let request = api.del(tags.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
};

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('tags', {
  search,
  getAll,
  get,
  create,
  update,
  remove
});
