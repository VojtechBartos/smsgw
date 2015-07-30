'use strict';

import EventListener from 'eventemitter3';
import {Map, List} from 'immutable';

class State extends EventListener {

  constructor() {
    super();
    this._state = Map();
  }

  set(state) {
    if (this._state === state) return;
    this._state = state;
    this.emit('change', this._state);
  }

  get() {
    return this._state;
  }

  cursor(path, defaultDataStructure = Map) {
    return (arg) => {
      if (!this._state.getIn(path))
        this._state = this._state.setIn(path, defaultDataStructure());

      if (!arg)
        return this._state.getIn(path);

      this.set(this._state.updateIn(path, arg));
    };
  }

}

export const state = new State();
export const pendingActionsCursor = state.cursor(['pendingActions']);
export const flashMessagesCursor = state.cursor(['flashMessages'], List);
export const usersCursor = state.cursor(['users']);
export const templatesCursor = state.cursor(['templates']);
export const applicationsCursor = state.cursor(['applications']);
export const contactsCursor = state.cursor(['contacts']);
export const contactsSearchCursor = state.cursor(['contactsSearch']);
export const outboxCursor = state.cursor(['outbox']);
export const tagsCursor = state.cursor(['tags']);
export const tagsSearchCursor = state.cursor(['tagsSearch']);
export const sentCursor = state.cursor(['sent']);
export const phonesCursor = state.cursor(['phones']);
export const inboxCursor = state.cursor(['inbox']);
