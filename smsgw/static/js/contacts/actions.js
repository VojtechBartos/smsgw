'use strict';

import Dispatcher from '../dispatcher';
import {contacts} from '../endpoints';
import setToString from '../lib/settostring';
import {getToken} from '../users/actions';
import * as api from '../api';

/**
 * Search tag by name
 * @param  {String} phrase
 */
export function search(phrase) {
  const token = getToken();
  const request = api.get(contacts.index(), {
    token,
    query: {
      search: phrase
    }
  });

  return Dispatcher.dispatch(search, request);
}

/**
 * Get all
 */
export function getAll() {
  const token = getToken();
  const request = api.get(contacts.index(), { token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Get specific
 * @param  {String} uuid
 */
export function get(uuid) {
  const token = getToken();
  const request = api.get(contacts.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
}

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  const token = getToken();
  const request = api.post(contacts.create(), { token, data });

  return Dispatcher.dispatch(create, request);
}

/**
 * Update
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  const token = getToken();
  const request = api.put(contacts.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
}

/**
 * Delete
 * @param  {String} uuid
 */
export function remove(uuid) {
  const token = getToken();
  const request = api.del(contacts.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('contacts', {
  search,
  getAll,
  get,
  create,
  update,
  remove
});
