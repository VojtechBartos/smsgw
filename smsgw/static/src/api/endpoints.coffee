###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

BASE = "/api/1.0"

module.exports = 
    users:
        me: -> "#{BASE}/users/@me/"
        signIn: -> "#{BASE}/auth/login/"
        index: -> "#{BASE}/users/"
        create: -> "#{BASE}/users/"
        get: (uuid) -> "#{BASE}/users/#{uuid}/"
        update: (uuid) -> @get uuid
        delete: (uuid) -> @get uuid
    contacts:
        index: (user = "@me") -> "#{BASE}/users/#{user}/contacts/"
        create: (user = "@me") -> "#{BASE}/users/#{user}/contacts/"
        get: (uuid, user = "@me") -> "#{BASE}/users/#{user}/contacts/#{uuid}/"
        update: (uuid, user = "@me") -> @get uuid, user
        delete: (uuid, user = "@me") -> @get uuid, user
    templates:
        index: (user = "@me") -> "#{BASE}/users/#{user}/templates/"
        create: (user = "@me") -> "#{BASE}/users/#{user}/templates/"
        get: (uuid, user = "@me") -> "#{BASE}/users/#{user}/templates/#{uuid}/"
        delete: (uuid, user = "@me") -> @get uuid, user
