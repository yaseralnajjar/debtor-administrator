const webpack = require('webpack')

//const IS_PRODUCTION = process.env.HOST_ENV === 'production'


module.exports = {
    outputDir: 'dist',
    assetsDir: 'static',

    configureWebpack: {
      plugins: [
        new webpack.EnvironmentPlugin(['GOOGLE_OAUTH_CLIENT_ID']),
      ],
    },

    // baseUrl: IS_PRODUCTION
    // ? 'http://cdn123.com'
    // : '/',
    // For Production, replace set baseUrl to CDN
    // And set the CDN origin to `yourdomain.com/static`
    // Whitenoise will serve once to CDN which will then cache
    // and distribute
    devServer: {
      proxy: {
        '/api*': {
          // Forward frontend dev server request for /api to django dev server
          target: 'http://localhost:8000/',
        }
      }
    }
  }
