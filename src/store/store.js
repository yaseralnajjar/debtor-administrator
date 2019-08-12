import Vue from "vue";
import Vuex from "vuex";
import $backend from '@/backend';
Vue.prototype.$backend = $backend;
import actions from './actions'
import mutations from './mutations'
import getters from './getters'
Vue.use(Vuex);


let isAuth = localStorage.getItem('auth')
let name = ''
if(isAuth){
    name = JSON.parse(localStorage.getItem('auth')).user_full_name
}

export default new Vuex.Store({
    state: {
        authStatus: '',
        isAuth: isAuth,
        name: name,
        isAllowed: true
    },

    getters,
    mutations,
    actions
});  