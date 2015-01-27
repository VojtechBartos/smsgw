###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/TagConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

_tags = {}

save = (data) ->
    for item in data
        _tags[item.uuid] = item

TagStore = createStore Dispatcher,
    getAll: -> (val for key, val of _tags)
    get: (uuid) -> 
        _tags[uuid]        

TagStore.listenTo constants.TAG_SEARCH, (payload) ->
    _tags = payload.data
    @emitChange()

module.exports = TagStore