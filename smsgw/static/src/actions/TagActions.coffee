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

    fetchAll: ->
        url = endpoints.index()
        req = api.fetch 'GET', url, token: UserActions.token

        Dispatcher.dispatchRequest req, constants.TAG_FETCH_ALL

    fetch: (uuid) ->
        url = endpoints.get uuid
        req = api.fetch 'GET', url, token: UserActions.token

        Dispatcher.dispatchRequest req, constants.TAG_UPDATE

    create: (data) ->
        url = endpoints.create()
        req = api.fetch 'POST', url, 
            token: UserActions.token        
            data: data

        Dispatcher.dispatchRequest req, constants.TAG_UPDATE

    update: (uuid, data) ->
        url = endpoints.update uuid
        req = api.fetch 'PUT', url,
            token: UserActions.token        
            data: data

        Dispatcher.dispatchRequest req, constants.TAG_UPDATE

    delete: (uuid) ->
        url = endpoints.delete uuid
        req = api.fetch 'DELETE', url, token: UserActions.token

        Dispatcher.dispatchRequest req, constants.TAG_DELETE