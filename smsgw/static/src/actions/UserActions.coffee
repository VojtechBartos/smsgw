###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

Dispatcher = require '../dispatcher.coffee'
constants = require '../constants/UserConstants.coffee'
endpoints = require('../api/endpoints.coffee').users
localStorage = require 'localStorage'
api = require '../api/index.coffee'

module.exports =

    token: localStorage.getItem 'token'

    setToken: (token) ->
        localStorage.setItem 'token', token

    signUp: (data) ->
        url = endpoints.create()
        req = api.fetch 'POST', url, data: data

        Dispatcher.dispatchRequest req, constants.USER_SIGN_UP

    signIn: (data) ->
        url = endpoints.signIn()
        req = api.fetch 'POST', url, data: data

        Dispatcher.dispatchRequest req, constants.USER_SIGN_IN

    signOut: ->
        localStorage.removeItem 'token'

    fetchMe: ->
        url = endpoints.get "@me"
        req = api.fetch 'GET', url, token: @token

        Dispatcher.dispatchRequest req, constants.USER_FETCH_ME