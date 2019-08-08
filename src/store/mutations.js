export default {
    auth_success(state) {
        state.authStatus = 'Success'
        state.isAuth = !!localStorage.getItem('auth')
        state.name = JSON.parse(localStorage.getItem('auth')).user_full_name
    },
    auth_error(state) {
        state.authStatus = 'An error occur'
    },
    logout(state) {
        state.isAuth = null
    },
    notAllowed(state) {
        state.isAllowed = false
    },
    clearNotAllowed(state) {
        state.isAllowed = true
    },
}