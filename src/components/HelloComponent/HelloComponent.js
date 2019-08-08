export default {
  name: 'HelloComponent',
  data() {
    return {
      user: {},
      googleSignInParams: {
        client_id: '693415395547-5vu6ctkm4979fte6c48ub7vdb51fsurj.apps.googleusercontent.com'
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
      console.log('OH NOES', error)
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0
    }
  }
}