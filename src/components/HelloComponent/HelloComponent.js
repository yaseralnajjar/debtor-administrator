export default {
  name: 'HelloComponent',
  data() {
    return {
      user: {},
      googleSignInParams: {
        client_id: '693415395547-p47sfv65kq7culuf2u1ci74gqbb73e6p.apps.googleusercontent.com'
      }
    }
  },
  methods: {
    onGoogleSignInSuccess(user) {
      const token = user.Zi.access_token
      const userFullName = user.getBasicProfile().ig
      this.$store.dispatch('auth', { token,  userFullName})
      this.$router.push('debtors')
    },
    onGoogleSignInError(error) {
      console.log('OH NOES', error)
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0
    }
  }
}