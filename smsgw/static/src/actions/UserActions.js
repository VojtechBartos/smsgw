'use strict';

import Dispatcher from '../dispatcher';
import constants from '../constants/UserConstants';
import {users} from '../api/endpoints';
import localStorage from 'localStorage';
// TODO(vojta) undefined via import from, dont know why, hack for now
let api = require('../api/index.js');
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
 * Sign up
 * creating new user
 * @param {Object} data payload
 */
export function signUp(data) {
  let req = api.post(users.create(), { data: data });

  Dispatcher.dispatchRequest(req, constants.USER_SIGN_UP);
}

/**
 * Sign in
 * @param {Object} data payload
 */
export function signIn(data) {
  let req = api.post(users.signIn(), { data: data });

  Dispatcher.dispatchRequest(req, constants.USER_SIGN_IN);
}

/**
 * Sign out
 * removing token from localstorage
 */
export function signOut() {
  _token = null;
  localStorage.removeItem('token');
}

/**
 * Fetch current user
 */
export function fetchMe() {
  let req = api.get(users.get('@me'), { token: _token });

  Dispatcher.dispatchRequest(req, constants.USER_FETCH_ME);
}

/**
 * Fetch all users
 */
export function fetchAll() {
  let req = api.get(users.index(), { token: _token });

  Dispatcher.dispatchRequest(req, constants.USER_FETCH_ALL);
}

/**
 * Fetch specific user by uuid
 * @param  {String} uuid of user
 */
export function fetch(uuid) {
  let req = api.get(users.get(uuid), { token: _token });

  Dispatcher.dispatchRequest(req, constants.USER_UPDATE);
}

/**
 * Create new user
 * @param  {Object} data payload
 */
export function create(data) {
  let req = api.post(users.create(), {
    token: _token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.USER_UPDATE);
}

/**
 * Update user
 * @param  {String} uuid of user
 * @param  {Object} data payload
 */
export function update(uuid, data) {
  let req = api.put(users.update(uuid), {
    token: _token,
    data: data
  });

  Dispatcher.dispatchRequest(req, constants.USER_UPDATE);
}

/**
 * Reset password
 * @param {String} uuid of user
 * @param {Object} data payload
 */
export function resetPassword(uuid, data) {
  let req = api.post(users.resetPasswprd(uuid), { data: data });

  Dispatcher.dispatchRequest(req, constants.USER_DELETE);
}

/**
 * Delete user
 * @param  {String} uuid of user
 */
export function del(uuid) {
  let req = api.del(users.del(uuid), { token: _token });

  Dispatcher.dispatchRequest(req, constants.USER_DELETE);
}
