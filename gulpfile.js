/**
 * https://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml
 */
"use strict";

var gulp = require('gulp');
var gulpWebpack = require('gulp-webpack');
var webpack = require('webpack');
var sh = require('execSync'); // TODO(vojta) replace by native in node 0.12
var isDevelopment = true;

/**
 * Webpack
 */
gulp.task('webpack', function() {
  gulp
    .src('./smsgw/static/src/main.js')
    .pipe(gulpWebpack({
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
      },
      plugins: (function() {
        // get git tag
        var result = sh.exec('git describe');
        var tag = (result.code === 0) ? result.stdout : new Date().getTime();

        var plugins = [
          new webpack.DefinePlugin({
            'process.env': {
              NODE_ENV: JSON.stringify((isDevelopment) ? 'development' : 'production')
            },
            __VERSION__: JSON.stringify(tag),
            __DEV__: (isDevelopment)
          })
        ];

        if (!isDevelopment) {
          plugins = plugins.concat([
            new webpack.optimize.DedupePlugin(),
            new webpack.optimize.OccurenceOrderPlugin(),
            new webpack.optimize.UglifyJsPlugin({
              compress: { warnings: false },
              output: { comments: false }
            })
          ]);
        }
        return plugins;
      })(),
    }))
    .pipe(gulp.dest('./smsgw/static/build/'));
});

/**
 * Default task
 */
gulp.task('default', ['webpack']);
