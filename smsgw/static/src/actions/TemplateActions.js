'use strict';

import Dispatcher from '../dispatcher';
import constants from '../constants/TemplateConstants';
import {templates} from '../api/endpoints';
// TODO(vojta) undefined via import from, dont know why, hack for now
let api = require('../api/index.js');
let UserActions = require('./UserActions');

/**
 * Fetch all
 */
export function fetchAll() {
  let req = api.get(templates.index(), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.TEMPLATE_FETCH_ALL);
};

/**
 * Fetch specific template
 * @param  {String} uuid
 */
export function fetch(uuid) {
  let req = api.get(templates.get(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constantsTEMPLATEG_UPDATE);
};

/**
 * Create new template
 * @param  {Object} data
 */
export function create(data) {
  let req = api.post(templates.create(), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.TEMPLATE_UPDATE);
};

/**
 * Update template
 * @param  {String} uuid
 * @param  {Object} data
 */
export function update(uuid, data) {
  let req = api.put(templates.update(uuid), {
    token: UserActions.token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.TEMPLATE_UPDATE);
};

/**
 * Delete template
 * @param  {String} uuid
 */
export function del(uuid) {
  let req = api.del(templates.del(uuid), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.TEMPLATE_DELETE);
};
