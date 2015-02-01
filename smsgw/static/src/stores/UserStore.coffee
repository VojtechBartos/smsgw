###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/UserConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

UserStore = createStore Dispatcher,
    me: -> @get yes, '@me'

UserStore.listenTo constants.USER_SIGN_UP, (payload) ->
    @emitChange payload.data

UserStore.listenTo constants.USER_SIGN_IN, (payload) ->
    @emitChange payload.data

UserStore.listenTo constants.USER_FETCH_ME, (payload) ->
    payload.data['@me'] = yes
    @update [payload.data]
    @emitChange()

UserStore.listenTo constants.USER_FETCH_ALL, (payload) ->
    @update payload.data
    @emitChange()

UserStore.listenTo constants.USER_UPDATE, (payload) ->
    @update [payload.data]
    @emitChange()

UserStore.listenTo constants.USER_DELETE, (payload) ->
    @delete payload.data.uuid
    @emitChange()

UserStore.listenTo constants.USER_ERROR, (payload) ->
    @emitError payload.error

module.exports = UserStore