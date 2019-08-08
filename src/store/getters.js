export default {
    isLoggedIn: state => !!state.isAuth,
    name: state => state.name,
    isAllowed: state => state.isAllowed
}