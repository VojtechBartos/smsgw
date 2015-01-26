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


module.exports = 
    fetch: (method, url, options) ->
        req = null
        switch method
            when 'POST'
                req = request.post
            when 'GET'
                req = request.get
            when 'PUT'
                req = request.put
            when 'DELETE'
                req = request.del
        
        new Promise (resolve, reject) ->
            req = req(url)
                    .accept 'application/json'
                    .type 'application/json'
            if options.token?                    
                req = req.set "Authorization", "Token #{options.token}" 
            req = req.send options.data if options.data?
            req = req.query options.query if options.query?
            req.end (res) ->
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