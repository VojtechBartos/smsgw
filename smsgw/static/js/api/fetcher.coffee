###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

Promise = require 'bluebird'
request = require 'superagent'
localStorage = require 'localStorage'

class ApiError extends Error
    # bad request url
    @url = null 
    # request method
    @method = null
    # request response code
    @status = null
    # message of error, taken from meta or error message
    @message = null
    # data content from response body
    @data = null

standartize = (req, token = null, query = {}) ->

    req = req
        .accept 'application/json'
        .type 'application/json'
    req = req.set("Authorization", "Token #{token}") if token?
    req

handler = (resolve, reject) ->
    (res) ->
        body = res.body
        if res.ok is yes
            resolve body
        else
            error = new ApiError()
            error.message = res.error.message
            error.status = res.status
            error.url = res.req.url

            if body
                if 'data' of body
                    error.data = body.data
                if 'meta' of body and 'message' of body.meta
                    error.message = body.meta.message
        
            reject error

module.exports = 

    get: (url, token, query = {}) ->
        new Promise (resolve, reject) ->
            standartize request.get(url), token, query
                .end handler resolve, reject

    post: (url, token, data = {}, query = {}) ->
        new Promise (resolve, reject) ->
            standartize request.post(url), token, query
                .send data
                .end handler resolve, reject

    put: (url, token, data = {}, query = {}) ->
        new Promise (resolve, reject) ->
            standartize request.put(url), token, query
                .send data
                .end handler resolve, reject

    delete: (url, token, query = {}) ->
        new Promise (resolve, reject) ->
            standartize request.del(url), token, query
                .end handler resolve, reject

