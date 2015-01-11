###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

keyMirror = require 'react/lib/keyMirror'

module.exports = 
    ACTION:
        FETCH: 
            ME: 'USER_ACTION_FETCH_ME'
        SIGN: 
            IN: 'USER_ACTION_SIGN_IN'
            OUT: 'USER_ACTION_SIGN_OUT'
            UP: 'USER_ACTION_SIGN_UP'
    EVENT:
        FETCH: 
            ME: 'USER_EVENT_FETCH_ME'
        SIGN:
            IN: 'USER_EVENT_SIGN_IN'
            OUT: 'USER_EVENT_SIGN_OUT'
