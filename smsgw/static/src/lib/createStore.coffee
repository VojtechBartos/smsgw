###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

EventEmitter = require('events').EventEmitter
_ = require 'lodash'

EVENT_CHANGE = 'change'
EVENT_ERROR = 'error'

module.exports = (dispatcher, definition = {}) ->
    # list of all handlers for dispatcher
    handlers = {}

    # shared API cross user stores
    store = _.assign {}, EventEmitter.prototype,
        _store: []

        getAll: (sortBy = 'created', asc = yes) -> 
            _.sortBy @_store, sortBy

        get: (value, attr = 'uuid') ->
            result = _.find @_store, (i) -> i[attr] == value
            result || null

        update: (rows, attr = 'uuid') ->
            for row in rows
                index = _.findKey @_store, (i) -> i[attr] == row[attr]
                if index?
                    @_store[index] = _.assign @_store[index], row
                else
                    @_store.push row

        delete: (value, attr = 'uuid') ->
            index = _.findKey @_store, (i) -> i[attr] == value
            @_store.splice index, 1

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

        listenTo: (actions, handler) ->
            if _.isArray actions
                for action in actions
                    handler[action] = handler.bind @
            else
                handlers[actions] = handler.bind @

    , definition

    # register dispatcher
    dispatcher.register (payload) ->
        if payload.action of handlers
            if 'success' of payload and payload.success is no
                store.emitError payload.error
            else
                handlers[payload.action](payload)            

    # prepared store to user
    store