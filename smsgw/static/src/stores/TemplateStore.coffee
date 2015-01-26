###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/TemplateConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

_templates = {}

save = (data) ->
    for item in data
        _templates[item.uuid] = item

TemplateStore = createStore Dispatcher,
    getAll: -> (val for key, val of _templates)
    get: (uuid) -> _templates[uuid]        

TemplateStore.listenTo constants.TEMPLATE_FETCH_ALL, (payload) ->
    save payload.data
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_FETCH, (payload) ->
    save [payload.data]
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_CREATE, (payload) ->
    save [payload.data]
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_UPDATE, (payload) ->
    save [payload.data]
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_DELETE, (payload) ->
    delete _templates[payload.data.uuid]
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_ERROR, (payload) ->
    @emitError payload.error

module.exports = TemplateStore