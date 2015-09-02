'use strict';

import * as actions from './actions';
import {outboxCursor} from '../state';
import Dispatcher from '../dispatcher';
import Message from './message';

/**
 * Get all
 */
export function getAll(applicationUuid) {
  return outboxCursor().filter(outbox => {
    const app = outbox.application;
    return (!app || app.uuid === applicationUuid);
  }).sort((a, b) => a > b);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      outboxCursor(outbox => {
        return outbox.clear().withMutations(items => {
          data.forEach(i => items.set(i.id, new Message(i)) );
        });
      });
      break;

    case actions.get:
      outboxCursor(outbox => {
        return outbox.set(data.id, new Message(data));
      });
      break;

    case actions.remove:
      outboxCursor(outbox => {
        return outbox.remove(data.id);
      });
      break;
  }
});
