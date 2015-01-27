###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/ContactConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

_contacts = {}

save = (data) ->
    for item in data
        _contacts[item.uuid] = item

ContactStore = createStore Dispatcher,
    getAll: -> (val for key, val of _contacts)
    get: (uuid) -> 
        _contacts[uuid]        

ContactStore.listenTo constants.CONTACT_FETCH_ALL, (payload) ->
    save payload.data
    @emitChange()

ContactStore.listenTo constants.CONTACT_FETCH, (payload) ->
    save [payload.data]
    @emitChange()

ContactStore.listenTo constants.CONTACT_CREATE, (payload) ->
    save [payload.data]
    @emitChange()

ContactStore.listenTo constants.CONTACT_UPDATE, (payload) ->
    save [payload.data]
    @emitChange()

ContactStore.listenTo constants.CONTACT_DELETE, (payload) ->
    delete _contacts[payload.data.uuid]
    @emitChange()

ContactStore.listenTo constants.CONTACT_ERROR, (payload) ->
    @emitError payload.error

module.exports = ContactStore