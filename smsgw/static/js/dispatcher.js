'use strict';

import flux from 'flux';
import {flash} from './flashMessages/actions';
import {pendingActionsCursor} from './state';

class Dispatcher extends flux.Dispatcher {

  dispatch(action, data) {
    if (data && typeof data.then === 'function')
      return this.dispatchAsync(action, data);
    else
      super.dispatch({action, data});
  }

  dispatchAsync(action, promise) {
    const name = action.toString();

    // pending property is defined lazily.
    if (!action.hasOwnProperty('pending'))
      Object.defineProperty(action, 'pending', {
        get: () => this.isPending(name)
      });

    this.setPending(name, true);
    return promise.then(body => {
      const {data, meta} = body

      this.setPending(name, false);
      super.dispatch({action, data, meta});

      return body;
    }).error(err => {
      this.setPending(name, false);

      super.dispatch({
        action: flash,
        data: { text: err.message, type: 'danger' }
      });

      throw err;
    });
  }

  setPending(name, pending) {
    pendingActionsCursor(actions => {
      return pending ? actions.set(name, true) : actions.delete(name);
    });
  }

  isPending(name) {
    return pendingActionsCursor().has(name);
  }

}

export default new Dispatcher()
