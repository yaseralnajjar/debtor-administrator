import Vue from "vue";
import Vuex from "vuex";
import $backend from '@/backend';
Vue.prototype.$backend = $backend;
import actions from './actions'
import mutations from './mutations'
import getters from './getters'
Vue.use(Vuex);


export default new Vuex.Store({
    state: {
        authStatus: '',
        isAuth: localStorage.getItem('auth'),
    },

    getters,
    mutations,
    actions
});  