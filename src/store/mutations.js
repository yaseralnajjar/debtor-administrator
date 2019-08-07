export default {
    auth_success(state) {
        state.authStatus = 'Success'
        state.isAuth = !!localStorage.getItem('auth')
    },
    auth_error(state) {
        state.authStatus = 'An error occur'
    },
    logout(state) {
        state.isAuth = null
    }
}