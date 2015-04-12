'use strict';

import Dispatcher from '../dispatcher';
import constants from '../constants/OutboxConstants';
import {outbox} from '../api/endpoints';
// TODO(vojta) undefined via import from, dont know why, hack for now
let api = require('../api/index.js');
let UserActions = require('./UserActions');

/**
 * Fetch all outbox messages
 */
export function fetchAll() {
  let req = api.get(outbox.index(), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.OUTBOX_FETCH_ALL);
};

/**
 * Delete outbox message
 * @param  {Integer} id 
 */
export function del(id) {
  let req = api.del(outbox.del(id), { token: UserActions.token });

  Dispatcher.dispatchRequest(req, constants.OUTBOX_DELETE);
};
