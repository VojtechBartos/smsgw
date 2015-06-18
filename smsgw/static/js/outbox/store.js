"use strict";

import _ from 'lodash';
import * as actions from './actions';
import {outboxCursor} from '../state';
import Dispatcher from '../dispatcher';
import Message from './message';

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