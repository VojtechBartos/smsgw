###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/ContactConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'
ContactStore = createStore Dispatcher

ContactStore.listenTo constants.CONTACT_FETCH_ALL, (payload) ->
    @update payload.data
    @emitChange()

ContactStore.listenTo constants.CONTACT_UPDATE, (payload) ->
    @update [payload.data]
    @emitChange()

ContactStore.listenTo constants.CONTACT_DELETE, (payload) ->
    @delete payload.data.uuid
    @emitChange()

ContactStore.listenTo constants.CONTACT_ERROR, (payload) ->
    @emitError payload.error

module.exports = ContactStore