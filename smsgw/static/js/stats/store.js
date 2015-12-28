'use strict';

import * as actions from './actions';
import {statsCursor} from '../state';
import Dispatcher from '../dispatcher';


/**
 * Registerting to dispatcher
 */
export const dispatchToken = Dispatcher.register(({action, data}) => {
  switch (action) {
    case actions.getStats:
      statsCursor(stats => {
        return stats.set('all', data);
      });
      break;

    case actions.getStatsForWeek:
      statsCursor(stats => {
        return stats.set('week', data);
      });
      break;

    case actions.getStatsForMonth:
      statsCursor(stats => {
        return stats.set('month', data);
      });
      break;
  }
});
