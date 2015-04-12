'use strict';

import Dispatcher from '../dispatcher';
import constants from '../constants/ContactConstants';
import {contacts} from '../api/endpoints';
// TODO(vojta) undefined via import from, dont know why, hack for now
let api = require('../api/index.js');
let UserActions = require('./UserActions');

/**
 * Fetch all contacts
 */
export function fetchAll() {
  let req = api.get(contacts.index(), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.CONTACT_FETCH_ALL);
};

/**
 * Fetch specific contanct
 * @param  {String} uuid
 */
export function fetch(uuid) {
  let req = api.get(contacts.get(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.CONTACT_UPDATE);
};

/**
 * Create new contact
 * @param  {Object} data
 */
export function create(data) {
  let req = api.post(contacts.create(), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.CONTACT_UPDATE);
};

/**
 * Update contact
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let req = api.put(contacts.update(uuid), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.CONTACTS_UPDATE);
};

/**
 * Delete contact
 * @param  {String} uuid
 */
export function del(uuid) {
  let req = api.del(contacts.del(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.CONTACT_DELETE);
};
