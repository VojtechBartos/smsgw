"use strict";

import gulp from 'gulp';
import gulpWebpack from 'webpack-stream';
import webpack from 'webpack';
import yargs from 'yargs';

const args = yargs
  .boolean('d')
  .alias('e', 'env')
  .default('e', 'development')
  .argv
const isRelease = (args.env == 'release')
const isDevelopment = (args.env == 'development');

/**
 * Webpack
 */
gulp.task('build', () => {
  return gulp
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
        let plugins = [
          new webpack.DefinePlugin({
            'process.env': {
              NODE_ENV: JSON.stringify((isDevelopment) ? 'development' : 'production')
            },
            __DEV__: (isDevelopment)
          })
        ];

        if (isRelease) {
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
gulp.task('default', ['build']);
