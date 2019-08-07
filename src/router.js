import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'hello',
      component: HelloComponent
    }
  ]
})
