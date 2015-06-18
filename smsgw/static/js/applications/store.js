"use strict";

import _ from 'lodash';
import * as actions from './actions';
import {applicationsCursor} from '../state';
import Dispatcher from '../dispatcher';
import Application from './application';

/**
 * Get by uuid
 * @param  {String} uuid
 */
export function get(uuid) {
  return applicationsCursor().get(uuid);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case actions.getAll:
      applicationsCursor(applications => {
        return applications.withMutations(items => {
          data.forEach(i => items.set(i.uuid, new Application(i)) );
        });
      });
      break;

    case actions.regenerateToken:
      applicationsCursor(applications => {
        return applications.setIn([data.uuid, 'token'], data.token);
      });
      break;

    case actions.update:
    case actions.get:
      applicationsCursor(applications => {
        return applications.set(data.uuid, new Application(data));
      });
      break;

    case actions.remove:
      applicationsCursor(applications => {
        return applications.remove(data.uuid);
      });
      break;
  }
});
