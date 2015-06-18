"use strict";

import {flash} from './actions';
import {flashMessagesCursor} from '../state';
import Dispatcher from '../dispatcher';

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case flash:
      flashMessagesCursor(messages => {
        // TODO(vojta) if we wanna add close button this needs to be refactored
        // to remove item at specific index/hash
        setTimeout(() => {
          flashMessagesCursor(messages => {
            return messages.delete(0);
          });
        }, 5000);

        return messages.push(data);
      });
      break;
  }
});
