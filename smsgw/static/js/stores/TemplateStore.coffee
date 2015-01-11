###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

TemplateConstants = require '../constants/TemplateConstants.coffee'
createStore = require '../lib/createStore.coffee'
Dispatcher = require '../dispatcher.coffee'

_templates = []

TemplateStore = createStore Dispatcher,
    getAll: -> _templates
    get: (uuid) ->
        item = null
        for template in _templates
            if template.uuid == uuid
                item = template
                break
        item
            
TemplateStore.listenTo TemplateConstants.ACTION.FETCH.ALL, (payload) ->
    if payload.success
        _templates = payload.data
        @emitChange()
    else 
        @emitError payload.error

TemplateStore.listenTo TemplateConstants.ACTION.GET, (payload) ->
    if payload.success
        _templates.push payload.data
        @emitChange()
    else 
        @emitError payload.error

TemplateStore.listenTo TemplateConstants.ACTION.ADD, (payload) ->
    if payload.success
        _templates.push payload.data
        @emitChange()
    else
        @emitError payload.error

TemplateStore.listenTo TemplateConstants.ACTION.DELETE, (payload) ->
    if payload.success
        _templates = _templates.filter (item) -> item.uuid != payload.data.uuid
        @emitChange()
    else
        @emitError payload.error

module.exports = TemplateStore