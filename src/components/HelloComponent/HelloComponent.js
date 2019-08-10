export default {
  name: 'HelloComponent',
  data() {
    return {
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
    },
    onGoogleSignInError(error) {
      //console.log('OH NOES', error)
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0
    }
  }
}