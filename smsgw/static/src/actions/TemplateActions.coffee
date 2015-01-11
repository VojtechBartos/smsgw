###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

Dispatcher = require '../dispatcher.coffee'
TemplateConstants = require '../constants/TemplateConstants.coffee'
api = require '../api/fetcher.coffee'
endpoints = require('../api/endpoints.coffee').templates

UserActions = require './UserActions.coffee'



module.exports =

    fetchAll: ->
        url = endpoints.index()
        api.get url, UserActions.token
            .then ({meta, data}) ->
                console.log TemplateConstants.ACTION.FETCH.ALL
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.FETCH.ALL
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.ERROR
                    success: no
                    error: err

    get: (uuid) ->
        api.get endpoints.get uuid, UserActions.token
            .then ({meta, data}) ->
                console.log TemplateConstants.ACTION.GET
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.GET
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.GET
                    success: no
                    error: err

    add: (data) ->
        api.post endpoints.create(), UserActions.token, data
            .then ({meta, data}) ->
                console.log TemplateConstants.ACTION.ADD
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.ADD
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.ERROR
                    success: no
                    error: err

    delete: (uuid) ->
        url = endpoints.delete(uuid)
        api.delete url, UserActions.token
            .then ({meta, data}) ->
                console.log TemplateConstants.ACTION.DELETE
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.DELETE
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: TemplateConstants.ACTION.ERROR
                    success: no
                    error: err

