var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var config = require('./webpack.base.config.js');
var ip = 'localhost'

//add as many entry points as you have container-react-components
config.entry = {
  Index: [
    'webpack-dev-server/client?http://' + ip + ':3000',
    'webpack/hot/only-dev-server',
    'react-hot-loader/patch',
    path.join(__dirname, '../static/js/src/main/Index')
  ],
  vendors: ['react'],
};

config.devtool = 'inline-sourcemap';
config.output = {
  path: path.join(__dirname, '../static/builds-development/'),
  filename: '[name]-[hash].js',
  publicPath: 'http://'+ ip + ':3000/static/builds/',
};

config.plugins = [
  new webpack.HotModuleReplacementPlugin(),
  new BundleTracker({ filename: './webpack/webpack-stats.dev.json' }),
  new webpack.DefinePlugin({
    'process.env': {
      NODE_ENV: JSON.stringify('development'),
      BASE_URL: JSON.stringify('http://0.0.0.0:8000/'),
    }
  }),
  new webpack.optimize.CommonsChunkPlugin('vendors', 'vendors.js'), //seperates bundle files, one for react.js one for our app. Caches react library so users don't have to redownload.
];

config.module.loaders[0].query.plugins = ['react-hot-loader/babel'];

config.devServer = {
  inline: true,
  progress: true,
  hot: true,
  headers: { "Access-Control-Allow-Origin": "*" },
  historyApiFallback: true,
  host: '0.0.0.0',
  port: 3000
};

module.exports = config;
