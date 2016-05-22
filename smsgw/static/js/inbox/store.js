'use strict';

import * as actions from './actions';
import {inboxCursor} from '../state';
import Dispatcher from '../dispatcher';
import Message from './message';

/**
 * Get all
 */
export function getAll(applicationUuid) {
  return inboxCursor().filter(inbox => {
    const app = inbox.application;
    return (!app || app.uuid === applicationUuid);
  }).sort((a, b) => a.received < b.received);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      inboxCursor(inbox => {
        inbox = inbox.clear();
        return inbox.withMutations(items => {
          data.forEach(i => items.set(i.id, new Message(i)) );
        });
      });
      break;

    case actions.remove:
      inboxCursor(inbox => {
        return inbox.remove(data.id);
      });
      break;
  }
});
