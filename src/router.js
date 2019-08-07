import Vue from 'vue'
import Router from 'vue-router'
import HelloComponent from './components/HelloComponent/HelloComponent.vue'
import DebtorsComponent from './components/DebtorsComponent/DebtorsComponent.vue'

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
      component: DebtorsComponent
    }
  ]
})
