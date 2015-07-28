'use strict';

import * as actions from './actions';
import {phonesCursor} from '../state';
import Dispatcher from '../dispatcher';
import Phone from './phone';


/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getAll:
      phonesCursor(phones => {
        return phones.withMutations(items => {
          data.forEach(i => items.set(i.id, new Phone(i)) );
        });
      });
      break;

  }
});
