###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

Dispatcher = require '../dispatcher'
UserActions = require './UserActions.coffee'
constants = require '../constants/OutboxConstants'
endpoints = require('../api/endpoints.coffee').outbox
api = require '../api/index.coffee'

module.exports =

    fetchAll: ->
        url = endpoints.index()
        req = api.fetch 'GET', url, token: UserActions.token

        Dispatcher.dispatchRequest req, constants.OUTBOX_FETCH_ALL

    delete: (id) ->
        url = endpoints.delete id
        req = api.fetch 'DELETE', url, token: UserActions.token

        Dispatcher.dispatchRequest req, constants.OUTBOX_DELETE