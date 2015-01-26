###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

EventEmitter = require('events').EventEmitter
assign = require 'object-assign'
EVENT_CHANGE = 'change'
EVENT_ERROR = 'error'

module.exports = (dispatcher, definition) ->
    # list of all handlers for dispatcher
    handlers = {}

    # shared API cross user stores
    store = assign({}, EventEmitter.prototype,
        emitChange: (data = null) ->
            @emit EVENT_CHANGE, data

        emitError: (err) ->
            @emit EVENT_ERROR, err

        addChangeListener: (callback) ->
            @on EVENT_CHANGE, callback

        removeChangeListener: (callback) ->
            @removeListener EVENT_CHANGE, callback

        addErrorListener: (callback) ->
            @on EVENT_ERROR, callback

        removeErrorListener: (callback) ->
            @removeListener EVENT_ERROR, callback

        listenTo: (action, handler) ->
            handlers[action] = handler.bind @

    , definition)

    # register dispatcher
    dispatcher.register (payload) ->
        if payload.action of handlers
            if 'success' of payload and payload.success is no
                store.emitError payload.error
            else
                handlers[payload.action](payload)            

    # prepared store to user
    store