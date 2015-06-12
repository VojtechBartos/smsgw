"use strict";

import Dispatcher from '../dispatcher';
import {users} from '../api/endpoints';
import localStorage from 'localStorage';
import setToString from '../lib/settostring';

// TODO(vojta) undefined via import from, dont know why, hack for now
const api = require('../api/index.js');
let _token = localStorage.getItem('token');


/**
 * User token
 */
export const token = _token;

/**
 * Setting up user token
 * @param {String} token hash
 */
export function setToken(token) {
  _token = token;

  localStorage.setItem('token', token);
}

/**
 * Fetch current user
 */
export function getLoggedIn() {
  let request = api.get(users.get('@me'), { token: _token });

  return Dispatcher.dispatch(getLoggedIn, request);
}

/**
 * Fetch all users
 */
export function getAll() {
  let request = api.get(users.index(), { token: _token });

  return Dispatcher.dispatch(getAll, request);
}

/**
 * Fetch specific user by uuid
 * @param  {String} uuid of user
 */
export function get(uuid) {
  let request = api.get(users.get(uuid), { token: _token });

  return Dispatcher.dispatch(get, request)
}

/**
 * Create new user
 * @param  {Object} data payload
 */
export function create(data) {
  let request = api.post(users.create(), {
    token: _token,
    data: data
  });

  return Dispatcher.dispatch(create, request);
}

/**
 * Update user
 * @param  {String} uuid of user
 * @param  {Object} data payload
 */
export function update(uuid, data) {
  let request = api.put(users.update(uuid), {
    token: _token,
    data: data
  });

  return Dispatcher.dispatch(update, request);
}

/**
 * Reset password
 * @param {String} uuid of user
 * @param {Object} data payload
 */
export function resetPassword(uuid, data) {
  let request = api.post(users.resetPasswprd(uuid), { data: data });

  return Dispatcher.dispatch(resetPasswprd, request);
}

/**
 * Delete user
 * @param  {String} uuid of user
 */
export function del(uuid) {
  let request = api.del(users.del(uuid), { token: _token });

  return Dispatcher.dispatch(del, request);
}

/**
 * Sign in
 * @param {Object} data payload
 */
export function signIn(data) {
  let request = api.post(users.signIn(), { data: data });

  return Dispatcher.dispatch(signIn, request).then(({data, meta}) => {
    setToken(data.token);
  });
}

/**
 * Sign up
 * creating new user
 * @param {Object} data payload
 */
export function signUp(data) {
  let request = api.post(users.create(), { data: data });

  return Dispatcher.dispatch(signUp, request);
}

/**
 * Sign out
 * removing token from localstorage
 */
export function signOut() {
  _token = null;
  localStorage.removeItem('token');
}

// Override toString methods. Pretty useful for dispatched actions monitoring.
setToString('users', {
  getLoggedIn,
  getAll,
  get,
  create,
  update,
  del,
  signIn,
  signUp,
  signOut,
  setToken
});
