'use strict';

import flux from 'flux';

class Dispatcher extends flux.Dispatcher {

  dispatchRequest(req, action) {
    self = this
    req.then(body => {
      let data = body.data
      let meta = body.meta

      setTimeout(() => {
        self.dispatch({
          action: action,
          success: true,
          meta: meta,
          data: data
        })
      })
    }).error(err => {
      action = action.split('_')
      action = `${action[0]}_ERROR`

      self.dispatch({
        action: action,
        success: false,
        error: err
      })
    })
  }

}

export default new Dispatcher()
