###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

Dispatcher = require '../dispatcher.coffee'
TemplateConstants = require '../constants/TemplateConstants.coffee'
api = require '../api/fetcher.coffee'
endpoints = require('../api/endpoints.coffee').templates



module.exports =

    fetchAll: ->
        url = endpoints.index()
        api.get url
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
        api.get endpoints.get uuid
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
        api.post endpoints.create(), data
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
        api.delete url
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

