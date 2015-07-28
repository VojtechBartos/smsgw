'use strict';

import * as actions from './actions';
import {sentCursor} from '../state';
import Dispatcher from '../dispatcher';
import Message from './message';

/**
 * Get by id
 * @param  {String} id
 */
export function get(id) {
  return sentCursor().get(id);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      sentCursor(sent => {
        return sent.withMutations(items => {
          data.forEach(i => items.set(i.id, new Message(i)) );
        });
      });
      break;

    case actions.remove:
      sentCursor(sent => {
        return sent.remove(data.id);
      });
      break;
  }
});
