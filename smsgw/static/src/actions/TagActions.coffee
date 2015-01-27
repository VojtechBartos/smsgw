###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

Dispatcher = require '../dispatcher.coffee'
UserActions = require './UserActions.coffee'
constants = require '../constants/TagConstants.coffee'
endpoints = require('../api/endpoints.coffee').tags
api = require '../api/index.coffee'

module.exports =

    search: (name) ->
        url = endpoints.index()
        req = api.fetch 'GET', url, 
            token: UserActions.token
            query:
                search: name

        Dispatcher.dispatchRequest req, constants.TAG_SEARCH
