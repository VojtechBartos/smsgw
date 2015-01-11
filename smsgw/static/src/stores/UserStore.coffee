###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

UserConstants = require '../constants/UserConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

_users = []

UserStore = createStore Dispatcher,
    getAll: -> _users
    get: (uuid) -> (user for user in _users when user.uuid is uuid)
    getMe: ->
        me = null
        for user in _users
            me = user if '_me' of user            
        me

UserStore.listenTo UserConstants.ACTION.SIGN.OUT, (data) ->
    @emit UserConstants.EVENT.SIGN.OUT

UserStore.listenTo UserConstants.ACTION.SIGN.UP, (data) ->
    @emit UserConstants.EVENT.SIGN.UP, data

UserStore.listenTo UserConstants.ACTION.SIGN.IN, (data) ->
    @emit UserConstants.EVENT.SIGN.IN, data

UserStore.listenTo UserConstants.ACTION.FETCH.ME, (data) ->
    @emit UserConstants.EVENT.FETCH.ME, data


module.exports = UserStore