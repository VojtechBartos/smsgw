"use strict";

import _ from 'lodash';
import {Record} from 'immutable'
import * as actions from '../actions/templates';
import {templatesCursor} from '../state';
import Dispatcher from '../dispatcher';

const TemplateRecord = Record({
  uuid: null,
  label: null,
  text: null,
  createdAt: null
});

class Template extends TemplateRecord {}


/**
 * Get template by uuid
 * @param  {String} uuid
 */
export function get(uuid) {
  return templatesCursor().get(uuid);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case actions.getAll:
      templatesCursor(templates => {
        return templates.withMutations(items => {
          data.forEach(i => items.set(i.uuid, new Template(i)) );
        });
      });
      break;

    case actions.update:
    case actions.get:
      templatesCursor(templates => {
        return templates.set(data.uuid, new Template(data));
      });
      break;

    case actions.remove:
      templatesCursor(templates => {
        return templates.remove(data.uuid);
      });
      break;
  }
});
