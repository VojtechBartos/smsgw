"use strict";

import Dispatcher from '../dispatcher';
import setToString from '../lib/settostring';

/**
 * Show flash message
 * @param  {String} message
 * @param  {String} type
 */
export function flash(text, type = "success") {
  Dispatcher.dispatch(flash, { text, type });
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('flashMessages', {
  flash
});
