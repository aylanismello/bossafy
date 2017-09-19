const webpack = require('webpack');
const path = require('path');

module.exports = {
    entry: __dirname,
    entry: './client/index.jsx',
    output: {
        path: __dirname,
        filename: './client/bundle.js'
    },
    resolve: {
        extensions: ['.js', '.jsx']
    },
    devtool: 'source-maps',
    module: {
      loaders: [
        { loader:  'babel-loader?presets[]=es2015,presets[]=react,plugins[]=transform-object-rest-spread&retainLines=true' }
      ]
    },
};
