export default {
  name: 'HelloComponent',
  data() {
    return {
      snackbarLoginFailed: false,
      user: {},
      googleSignInParams: {
        client_id: process.env.GOOGLE_OAUTH_CLIENT_ID
      }
    }
  },
  methods: {
    onGoogleSignInSuccess(user) {
      const token = user.Zi.access_token
      const userFullName = user.getBasicProfile().ig
      this.$store.dispatch('auth', { token,  userFullName})
                 .catch(() => { this.snackbarLoginFailed = true })
    },
    onGoogleSignInError() {
      this.$store.dispatch('logout')
      this.snackbarLoginFailed = true
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0
    }
  }
}