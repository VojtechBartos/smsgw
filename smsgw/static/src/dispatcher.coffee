###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

flux = require 'flux'
assign = require 'object-assign'

module.exports = assign new flux.Dispatcher(), 
    
    dispatchRequest: (req, action) ->
        self = this
        req.then ({meta, data}) ->
            setTimeout ->
                self.dispatch
                    action: action
                    success: yes
                    data: data
            , 500
        .error (err) ->
            action = action.split '_'
            action = "#{action[0]}_ERROR"
            self.dispatch
                action: action
                success: no
                error: err
