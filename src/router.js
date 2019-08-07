import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'
import DebtorsListComponent from './components/DebtorsListComponent/DebtorsListComponent.vue'

import store from '@/store/store'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '*',
      redirect: '/'
    },
    {
      path: '/',
      name: 'hello',
      component: HelloComponent
    },
    {
      path: '/debtors',
      name: 'debtors',
      component: DebtorsComponent,
      beforeEnter: (to, from, next) => { (!store.getters.isLoggedIn) ? next('/') : next() }
    }
  ]
})
