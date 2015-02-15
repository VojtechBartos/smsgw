###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

gulp = require 'gulp'
webpack = require 'gulp-webpack'

###
    Webpack
###
gulp.task 'webpack', ->
    gulp.src './smsgw/static/src/app.coffee'
        .pipe webpack
            watch: yes,
            output:
                filename: 'bundle.js'
            module:
                loaders: [
                    { test: /\.coffee$/, loaders: ['coffee', 'cjsx'] }
                ]
            devServer: false
            debug: false
            hot: false
        .pipe gulp.dest './smsgw/static/build/'

###
    Default task
###
gulp.task 'default', ['webpack']
