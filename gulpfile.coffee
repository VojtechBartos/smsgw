###
See for more information
http://arcturo.github.io/library/coffeescript/07_the_bad_parts.html
###
"use strict"

gulp = require 'gulp'
watch = require 'gulp-watch'
source = require 'vinyl-source-stream'
browserify = require 'browserify'


###
    Building coffee script files
###
gulp.task 'coffee', ->
    br = browserify './smsgw/static/src/app.coffee'
    br.transform 'debowerify', global: yes
    br.transform 'coffee-reactify'
    br.transform "envify"
    br.bundle()
        .pipe source 'bundle.js'
        .pipe gulp.dest './smsgw/static/build/'

###
    Watching files
###
gulp.task 'watch', ->
    gulp.watch 'smsgw/static/src/**/*.coffee', ['coffee']

###
    Default task
###
gulp.task 'default', ['coffee', 'watch']
