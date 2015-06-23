"use strict";

import gulp from 'gulp';
import gulpWebpack from 'gulp-webpack';
import webpack from 'webpack';
import sh from 'execSync'; // TODO(vojta) replace by native in node 0.12

const isDevelopment = true;

/**
 * Webpack
 */
gulp.task('webpack', () => {
  gulp
    .src('./smsgw/static/js/main.js')
    .pipe(gulpWebpack({
      cache: (isDevelopment),
      watch: (isDevelopment),
      devtool: (isDevelopment) ? 'eval' : '',
      output: {
        filename: "js/[name].js"
      },
      module: {
        preLoaders: [
          { test: /\.js$/, exclude: /node_modules/, loader: "eslint-loader"}
        ],
        loaders: [
          { test: /\.js$/, exclude: /node_modules/, loader: 'babel-loader' }
        ]
      },
      plugins: (() => {
        // get git tag
        const result = sh.exec('git describe');
        const tag = (result.code === 0) ? result.stdout : new Date().getTime();

        let plugins = [
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
      eslint: {
        configFile: './.eslintrc'
      }
    }))
    .pipe(gulp.dest('./smsgw/static/build/'));
});

/**
 * Default task
 */
gulp.task('default', ['webpack']);
