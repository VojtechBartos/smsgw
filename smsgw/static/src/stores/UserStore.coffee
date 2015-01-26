###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/UserConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

_users = {}

save = (data) ->
    for item in data
        _users[item.uuid] = item

UserStore = createStore Dispatcher,
    getAll: ->  (val for key, val of _users)
    get: (uuid) -> _users[uuid]
    me: ->
        me = null
        for uuid, user of _users
            if '@me' of user
                me = user
                break
        me

UserStore.listenTo constants.USER_SIGN_UP, (payload) ->
    @emitChange payload.data

UserStore.listenTo constants.USER_SIGN_IN, (payload) ->
    @emitChange payload.data

UserStore.listenTo constants.USER_FETCH_ME, (payload) ->
    user = payload.data
    user["@me"] = yes

    save [user]

    @emitChange()

UserStore.listenTo constants.USER_ERROR, (payload) ->
    @emitError()


module.exports = UserStore