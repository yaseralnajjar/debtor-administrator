import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'
import DebtorsListComponent from './components/DebtorsListComponent/DebtorsListComponent.vue'
import DebtorUpdateComponent from './components/DebtorUpdateComponent/DebtorUpdateComponent.vue'

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
      component: HelloComponent
    },
    {
      path: '/debtors',
      component: DebtorsListComponent,
      beforeEnter: (to, from, next) => { (!store.getters.isLoggedIn) ? next('/') : next() }
    },
    {
      path: '/debtors/update/:id',
      component: DebtorUpdateComponent,
      beforeEnter: (to, from, next) => { (!store.getters.isLoggedIn) ? next('/') : next() }
    }
  ]
})
