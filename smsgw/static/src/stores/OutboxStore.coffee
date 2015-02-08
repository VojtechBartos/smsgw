###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/OutboxConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'
OutboxStore = createStore Dispatcher

OutboxStore.listenTo constants.OUTBOX_FETCH_ALL, (payload) ->
    @update payload.data, 'id'
    @emitChange()

OutboxStore.listenTo constants.OUTBOX_DELETE, (payload) ->
    @delete payload.data.id, 'id'
    @emitChange()

OutboxStore.listenTo constants.OUTBOX_ERROR, (payload) ->
    @emitError payload.error

module.exports = OutboxStore