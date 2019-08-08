import $backend from '@/backend';


export default {
    auth({ commit }, data) {
        const { token, userFullName } = data
        return new Promise((resolve, reject) => {
          $backend.$googleLogin(token).then(responseDate => {
            localStorage.setItem('auth', JSON.stringify({
              user_full_name: userFullName,
            }))
            commit('auth_success')
            resolve(responseDate)
          })
            .catch(err => {
              localStorage.removeItem('auth')
              commit('auth_error')
              reject(err)
            })
        })
      },
      logout({ commit }) {
        return new Promise((resolve) => {
          commit('logout')
          localStorage.removeItem('auth')
          resolve()
        });
    },
    notAllowed({ commit }) {
      commit('notAllowed')
    },
    clearNotAllowed({ commit }) {
      commit('clearNotAllowed')
    }
}    