const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all',
    proxy: {
      '^/api': {
        target: process.env.VUE_APP_API_URL,
        changeOrigin: true
      },
    },
  }
})
