'use strict';

import Dispatcher from '../dispatcher';
import {stats} from '../endpoints';
import setToString from '../lib/settostring';
import {getToken} from '../users/actions';
import * as api from '../api';


export function getStats(application) {
  const token = getToken();
  const request = api.get(stats(application), { token });

  return Dispatcher.dispatch(getStats, request);
}

export function getStatsForWeek(application) {
  const token = getToken();
  const request = api.get(stats(application, 'lastweek'), { token });

  return Dispatcher.dispatch(getStatsForWeek, request);
}

export function getStatsForMonth(application) {
  const token = getToken();
  const request = api.get(stats(application, 'lastmonth'), { token });

  return Dispatcher.dispatch(getStatsForMonth, request);
}


// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('stats', {
  getStats,
  getStatsForWeek,
  getStatsForMonth
});
