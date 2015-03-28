###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/TagConstants'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher'
TagStore = createStore Dispatcher

TagStore.listenTo constants.TAG_FETCH_ALL, (payload) ->
    @update payload.data
    @emitChange()

TagStore.listenTo constants.TAG_SEARCH, (payload) ->
    @_store = payload.data
    @emitChange()

TagStore.listenTo constants.TAG_UPDATE, (payload) ->
    @update [payload.data]
    @emitChange()

TagStore.listenTo constants.TAG_DELETE, (payload) ->
    @delete payload.data.uuid
    @emitChange()

TagStore.listenTo constants.TAG_ERROR, (payload) ->
    @emitError payload.error

module.exports = TagStore