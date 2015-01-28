###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/ApplicationConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'
ApplicationStore = createStore Dispatcher

ApplicationStore.listenTo constants.APPLICATION_FETCH_ALL, (payload) ->
    @update payload.data
    @emitChange()

ApplicationStore.listenTo constants.APPLICATION_UPDATE, (payload) ->
    @update [payload.data]
    @emitChange()

ApplicationStore.listenTo constants.APPLICATION_DELETE, (payload) ->
    @delete payload.data.uuid
    @emitChange()

ApplicationStore.listenTo constants.APPLICATION_ERROR, (payload) ->
    @emitError payload.error

module.exports = ApplicationStore