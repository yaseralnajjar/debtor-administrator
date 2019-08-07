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
    getMsgs(){
      console.log('bqbq')
      this.$backend.$fetchMessages().then(resp => console.log(resp))
    }
  }
}