'use strict';

import Dispatcher from '../dispatcher';
import {outbox} from '../endpoints';
import setToString from '../lib/settostring';
import {token} from '../users/actions';
import * as api from '../api';

/**
 * Get all groups
 */
export function getAll() {
  let request = api.get(outbox.index(), { token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Create new
 * @param  {Object} data
 */
export function create(data) {
  const payload = {
    send: data.send,
    message: data.message,
    phoneNumbers: data.phoneNumbers || [],
    tags: (data.tags || []).map(tag => tag.uuid),
    contacts: (data.contacts || []).map(contact => contact.uuid)
  };
  const request = api.post(outbox.create(), { token, data: payload });

  return Dispatcher.dispatch(create, request);
}

/**
 * Validate
 * @param  {String} phoneNumber
 */
export function validate(phoneNumber) {
  const request = api.post(outbox.validate(), { token, data: { phoneNumber } });

  return Dispatcher.dispatch(validate, request);
}

/**
 * Delete
 * @param  {String} group id
 */
export function remove(id) {
  let request = api.del(outbox.delete(id), { token });

  return Dispatcher.dispatch(remove, request);
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('outbox', {
  getAll,
  remove,
  validate
});
