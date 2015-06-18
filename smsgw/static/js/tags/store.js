"use strict";

import _ from 'lodash';
import * as actions from './actions';
import {tagsCursor} from '../state';
import Dispatcher from '../dispatcher';
import Tag from './tag';

/**
 * Get by uuid
 * @param  {String} uuid
 */
export function get(uuid) {
  return tagsCursor().get(uuid);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case actions.getAll:
      tagsCursor(tags => {
        return tags.withMutations(items => {
          data.forEach(i => items.set(i.uuid, new Tag(i)) );
        });
      });
      break;

    case actions.update:
    case actions.get:
      tagsCursor(tags => {
        return tags.set(data.uuid, new Tag(data));
      });
      break;

    case actions.remove:
      tagsCursor(tags => {
        return tags.remove(data.uuid);
      });
      break;
  }
});
