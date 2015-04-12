'use strict';

import Dispatcher from '../dispatcher';
import constants from '../constants/TagConstants';
import {tags} from '../api/endpoints';
// TODO(vojta) undefined via import from, dont know why, hack for now
let api = require('../api/index.js');
let UserActions = require('./UserActions');

/**
 * Search tag by name
 * @param  {String} name
 */
export function search(name) {
  let req = api.get(tags.index(), {
    token: UserActions.token,
    query: {
      search: name
    }
  });

  Dispatcher.dispatchRequest(req, constants.TAG_SEARCH);
};

/**
 * Fetch all
 */
export function fetchAll() {
  let req = api.get(tags.index(), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.TAG_FETCH_ALL);
};

/**
 * Fetch specific tag
 * @param  {String} uuid
 */
export function fetch(uuid) {
  let req = api.get(tags.get(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.TAG_UPDATE);
};

/**
 * Create tag
 * @param  {Object} data
 */
export function create(data) {
  let req = api.post(tags.create(), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.TAG_UPDATE);
};

/**
 * Update tag
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let req = api.put(tags.update(uuid), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.TAG_UPDATE);
};

/**
 * Delete tag
 * @param  {String} uuid
 */
export function del(uuid) {
  let req = api.del(tags.del(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.TAG_DELETE);
};
