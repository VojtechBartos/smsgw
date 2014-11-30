###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

class AssertationError extends Error
    @name = 'AssertationError'

module.exports = (condition, message) ->
    if condition
        throw new AssertationError message
    