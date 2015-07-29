'use strict';

import * as actions from './actions';
import {sentCursor} from '../state';
import Dispatcher from '../dispatcher';
import Message from './message';

/**
 * Get all
 */
export function getAll(applicationUuid) {
  return sentCursor().filter(sent => {
    const app = sent.application;
    return (!app || app.uuid === applicationUuid);
  });
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      sentCursor(sent => {
        sent = sent.clear();
        return sent.withMutations(items => {
          data.forEach(i => items.set(i.uuid, new Message(i)) );
        });
      });
      break;

    case actions.remove:
      sentCursor(sent => {
        return sent.remove(data.uuid);
      });
      break;
  }
});
