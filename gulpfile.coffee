###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

gulp = require 'gulp'
gutil = require 'gulp-util'
source = require 'vinyl-source-stream'
browserify = require 'browserify'
watchify = require 'watchify'

FRONTED_FILES = 
    'main': './smsgw/static/js/app.coffee'
    'bundle': 'bundle.js'
    'directory': './smsgw/static/build/'

###
    Watchify, browserify on JS frontend files
###
gulp.task 'watch', ->
    bs = browserify FRONTED_FILES['main'], watchify.args
    bundler = watchify bs
    bundler.transform 'coffee-reactify'

    rebundle = ->
        bundler.bundle()
        .on('error', gutil.log.bind(gutil, 'Browserify Error'))
        .pipe source FRONTED_FILES['bundle']
        .pipe gulp.dest FRONTED_FILES['directory']

    bundler.on 'update', rebundle
    rebundle()

###
    Default task
###
gulp.task 'default', ['watch']
