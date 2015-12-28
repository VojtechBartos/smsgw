'use strict';

import {flash} from './actions';
import {flashMessagesCursor} from '../state';
import Dispatcher from '../dispatcher';

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case flash:
      flashMessagesCursor(messages => {
        // TODO(vojta) if we wanna add close button this needs to be refactored
        // to remove item at specific index/hash
        setTimeout(() => {
          flashMessagesCursor(messages => {
            return messages.clear();
          });
        }, 5000);

        return messages.clear().push(data);
      });
      break;
  }
});
