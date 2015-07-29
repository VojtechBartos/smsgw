'use strict';

import * as actions from './actions';
import {outboxGroupsCursor} from '../state';
import Dispatcher from '../dispatcher';
// import Message from './message';
import Group from './group';

/**
 * Get by id
 * @param  {String} id
 */
// export function get(id) {
//   return outboxCursor().get(id);
// }

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      outboxGroupsCursor(groups => {
        groups = groups.clear();
        return groups.withMutations(items => {
          data.forEach(i => items.set(i.id, new Group(i)) );
        });
      });
      break;

    case actions.remove:
      outboxGroupsCursor(groups => {
        return groups.remove(data.id);
      });
      break;
  }
});
