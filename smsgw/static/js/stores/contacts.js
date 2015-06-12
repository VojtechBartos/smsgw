"use strict";

import _ from 'lodash';
import {Record} from 'immutable'
import * as actions from '../actions/contacts';
import {contactsCursor} from '../state';
import Dispatcher from '../dispatcher';

const ContactRecord = Record({
  uuid: null,
  firstName: null,
  lastName: null,
  phoneNumber: null,
  email: null,
  note: null,
  tags: null,
  createdAt: null
});

class Contact extends ContactRecord {}


/**
 * Get by uuid
 * @param  {String} uuid
 */
export function get(uuid) {
  return contactsCursor().get(uuid);
}

/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data, meta}) => {
  switch (action) {
    case actions.getAll:
      contactsCursor(contacts => {
        return contacts.withMutations(items => {
          data.forEach(i => items.set(i.uuid, new Contact(i)) );
        });
      });
      break;

    case actions.update:
    case actions.get:
      contactsCursor(contacts => {
        return contacts.set(data.uuid, new Contact(data));
      });
      break;

    case actions.remove:
      contactsCursor(contacts => {
        return contacts.remove(data.uuid);
      });
      break;
  }
});
