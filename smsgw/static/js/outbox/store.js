'use strict';

import * as actions from './actions';
import {outboxCursor} from '../state';
import Dispatcher from '../dispatcher';
import Group from './group';

/**
 * Get all
 */
export function getAll(applicationUuid) {
  return outboxCursor().filter(outbox => {
    const app = outbox.application;
    return (!app || app.uuid === applicationUuid);
  });
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      outboxCursor(outbox => {
        return outbox.clear().withMutations(items => {
          data.forEach(i => items.set(i.id, new Group(i)) );
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
