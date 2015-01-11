###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

localStorage = require 'localStorage'
Dispatcher = require '../dispatcher.coffee'
UserConstants = require '../constants/UserConstants.coffee'
api = require '../api/fetcher.coffee'
endpoints = require('../api/endpoints.coffee').users
localStorage = require 'localStorage'

UserActions =

    token: localStorage.getItem 'token'
    setToken: (token) ->
        localStorage.setItem 'token', token

    signUp: (data) ->
        api.post endpoints.create(), @token, data
            .then ({meta, data}) ->
                Dispatcher.dispatch 
                    action: UserConstants.ACTION.SIGN.UP
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: UserConstants.ACTION.SIGN.UP
                    success: no
                    error: err

    signIn: (data) ->
        api.post endpoints.signIn(), @token, data
            .then ({meta, data}) ->
                Dispatcher.dispatch 
                    action: UserConstants.ACTION.SIGN.IN
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: UserConstants.ACTION.SIGN.IN
                    success: no
                    error: err

    signOut: ->
        localStorage.removeItem 'token'
        Dispatcher.dispatch
            action: UserConstants.ACTION.SIGN.OUT

    fetchMe: ->
        url = endpoints.get "@me"
        api.get url, @token
            .then ({meta, data}) ->
                console.log UserConstants.ACTION.FETCH.ME
                Dispatcher.dispatch 
                    action: UserConstants.ACTION.FETCH.ME
                    success: yes
                    data: data
            .error (err) ->
                Dispatcher.dispatch 
                    action: UserConstants.ACTION.SIGN.OUT
                    success: no

module.exports = UserActions
