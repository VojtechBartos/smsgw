/**
 * https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml
 */
"use strict";

var gulp = require('gulp');
var webpack = require('gulp-webpack');
var isDevelopment = true;

/**
 * Webpack
 */
gulp.task('webpack', function() {
  gulp
    .src('./smsgw/static/src/app.js')
    .pipe(webpack({
      cache: (isDevelopment),
      watch: (isDevelopment),
      devtool: (isDevelopment) ? 'eval' : '',
      output: {
        filename: "js/[name].js"
      },
      module: {
        loaders: [
          {
            test: /\.coffee$/,
            exclude: /node_modules/,
            loaders: ['coffee', 'cjsx']
          },
          {
            test: /\.js$/,
            exclude: /node_modules/,
            loader: 'babel-loader'
          }
        ]
      }
    }))
    .pipe(gulp.dest('./smsgw/static/build/'));
});

/**
 * Default task
 */
gulp.task('default', ['webpack']);