"use strict";

import Dispatcher from '../dispatcher';
import {contacts} from '../api/endpoints';
import setToString from '../lib/settostring';
import {token} from './users';

// TODO(vojta) undefined via import from, dont know why, hack for now
const api = require('../api/index.js');

/**
 * Get all
 */
export function getAll() {
  let request = api.get(contacts.index(), { token });

  return Dispatcher.dispatch(getAll, request);
};

/**
 * Get specific
 * @param  {String} uuid
 */
export function get(uuid) {
  let request = api.get(contacts.get(uuid), { token });

  return Dispatcher.dispatch(get, request);
};

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  let request = api.post(contacts.create(), { token, data });

  return Dispatcher.dispatch(create, request);
};

/**
 * Update
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let request = api.put(contacts.update(uuid), { token, data });

  return Dispatcher.dispatch(update, request);
};

/**
 * Delete
 * @param  {String} uuid
 */
export function remove(uuid) {
  let request = api.del(contacts.delete(uuid), { token });

  return Dispatcher.dispatch(remove, request);
};

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('contacts', {
  getAll,
  get,
  create,
  update,
  remove
});
