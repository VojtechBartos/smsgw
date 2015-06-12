"use strict";

import _ from 'lodash';
import {Record} from 'immutable'
import * as actions from '../actions/outbox';
import {outboxCursor} from '../state';
import Dispatcher from '../dispatcher';

const OutboxRecord = Record({
  id: null,
  destinationNumber: null,
  contact: null,
  text: null,
  send: null,
  created: null,
  upddate: null
});

class Outbox extends OutboxRecord {}


/**
 * Get by id
 * @param  {String} id
 */
export function get(id) {
  return outboxCursor().get(id);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case actions.getAll:
      outboxCursor(outbox => {
        return outbox.withMutations(items => {
          data.forEach(i => items.set(i.id, new Outbox(i)) );
        });
      });
      break;

    case actions.remove:
      outboxCursor(outbox => {
        return outbox.remove(data.id);
      });
      break;
  }
});
