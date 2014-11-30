###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

EventEmitter = require('events').EventEmitter
assign = require 'object-assign'
EVENT_CHANGE = 'change'

module.exports = (dispatcher, definition) ->
    # list of all handlers for dispatcher
    handlers = {}

    # shared API cross user stores
    store = assign({}, EventEmitter.prototype,
        emitChange: ->
            console.log 'EMIT'
            @emit EVENT_CHANGE

        addChangeListener: (callback) ->
            @on EVENT_CHANGE, callback

        removeChangeListener: (callback) ->
            @removeChangeListener EVENT_CHANGE, callback

        listenTo: (action, handler) ->
            handlers[action] = handler.bind @

    , definition)

    # register dispatcher
    dispatcher.register (payload) ->
        if payload.action of handlers
            handlers[payload.action](payload)

    # prepared store to user
    store