'use strict';

import BPromise from 'bluebird';
import request from 'superagent';
import localStorage from 'localStorage';
import _ from 'lodash';

/**
 * ApiError class
 */
class ApiError extends Error {

  constructor(...args) {
    super(...args);

    this.status = null;
    this.url = null;
    this.method = null;
    this.data = null;
  }

}

/**
 * Generic fetch method
 * @param  {String} method of http request
 * @param  {String} url path of endpoint
 * @param  {Object} options of request as query and payload
 * @return {Promise}
 */
let fetch = (method, url, options) => {
  options = options || {};

  return new BPromise((resolve, reject) => {
    let req;
    switch (method) {
      case 'GET': req = request.get; break;
      case 'POST': req = request.post; break;
      case 'PUT': req = request.put; break;
      case 'DELETE': req = request.del; break;
    }

    req = req(url)
          .accept('application/json')
          .type('application/json');

    if (_.has(options, 'token')) {
      req = req.set('Authorization', `Token ${options.token}`);
    }
    if (_.has(options, 'data') && options.data) {
      req = req.send(options.data);
    }
    if (_.has(options, 'query') && options.query) {
      req = req.query(options.query);
    }

    req.end((err, res) => {
      let body = res.body;
      if (res.ok) return resolve(body);

      let error = new ApiError(err.message);
      error.status = res.status;
      error.url = res.req.url;
      if (body) {
        if (_.has(body, 'data')) {
          error.data = body.data;
        }
        if (_.has(body, 'meta') && _.has(body.meta, 'message')) {
          error.message = body.meta.message;
        }
      }

      return reject(error);
    });
  });
};


/**
 * GET api request
 * @param  {String} url path of endpoint
 * @param  {Object} options of request as query and payload
 * @return {Promise}
 */
export function get(url, options = {}) {
  return fetch('GET', url, options);
}

/**
 * POST api request
 * @param  {String} url path of endpoint
 * @param  {Object} options of request as query and payload
 * @return {Promise}
 */
export function post(url, options = {}) {
  return fetch('POST', url, options);
}

/**
 * PUT api request
 * @param  {String} url path of endpoint
 * @param  {Object} options of request as query and payload
 * @return {Promise}
 */
export function put(url, options = {}) {
  return fetch('PUT', url, options);
}

/**
 * DELETE api request
 * @param  {String} url path of endpoint
 * @param  {Object} options of request as query and payload
 * @return {Promise}
 */
export function del(url, options = {}) {
  return fetch('DELETE', url, options);
}
