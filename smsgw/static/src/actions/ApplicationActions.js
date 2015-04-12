'use strict';

import Dispatcher from '../dispatcher';
// import UserActions from './UserActions';
import constants from '../constants/ApplicationConstants';
import {applications} from '../api/endpoints';
// TODO(vojta) undefined via import from, dont know why, hack for now
let api = require('../api/index.js');
let UserActions = require('./UserActions');

/**
 * Fetch all
 */
export function fetchAll() {
  let req = api.get(applications.index(), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.APPLICATION_FETCH_ALL);
}

/**
 * Fetch specific application
 * @param  {String} uuid
 */
export function fetch(uuid) {
  let req = api.get(applications.get(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.APPLICATION_UPDATE);
}

/**
 * Create application
 * @param  {Object} data
 */
export function create(data) {
  let req = api.post(applications.create(), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.APPLICATION_UPDATE);
}

/**
 * Update application
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let req = api.put(applications.update(uuid), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.APPLICATION_UPDATE);
}

/**
 * Regenerate token
 * @param {String} uuid
 */
export function regenerateToken(uuid) {
  let req = api.put(applications.regenerate(uuid), {token: UserActions.token});

  Dispatcher.dispatchRequest(req, constants.APPLICATION_UPDATE);
}

/**
 * Delete app
 * @param  {String} uuid
 */
export function del(uuid) {
  let req = api.del(applications.del(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.APPLICATION_DELETE);
}
