import Vue from 'vue'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' 
import '@/plugins/vuetify'

import GSignInButton from 'vue-google-signin-button'

import App from '@/App.vue'
import router from '@/router'
import store from "@/store/store"

import $backend from '@/backend'


Vue.prototype.$backend = $backend
Vue.config.productionTip = false

Vue.use(Vuetify)
Vue.use(GSignInButton)

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
