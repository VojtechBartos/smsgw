###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

constants = require '../constants/TemplateConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'
TemplateStore = createStore Dispatcher

TemplateStore.listenTo constants.TEMPLATE_FETCH_ALL, (payload) ->
    @update payload.data
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_UPDATE, (payload) ->
    @update [payload.data]
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_DELETE, (payload) ->
    @delete payload.data.uuid
    @emitChange()

TemplateStore.listenTo constants.TEMPLATE_ERROR, (payload) ->
    @emitError payload.error

module.exports = TemplateStore