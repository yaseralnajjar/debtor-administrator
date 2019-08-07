export default {
  name: 'DebtorUpdateComponent',
  data() {
    return {
      valid: false,
      debtorId: '',
      firstName: '',
      lastName: '',
      email: '',
      iban: '',
      nameRules: [
        v => !!v || 'Name is required',
      ],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
      ],
      ibanRules: [
        v => !!v || 'IBAN is required',
        v => /^[a-zA-Z]{2}[0-9]{2}\s?[a-zA-Z0-9]{4}\s?[0-9]{4}\s?[0-9]{3}([a-zA-Z0-9]\s?[a-zA-Z0-9]{0,4}\s?[a-zA-Z0-9]{0,4}\s?[a-zA-Z0-9]{0,4}\s?[a-zA-Z0-9]{0,3})?$/.test(v) || 'IBAN must be valid',
      ]
    }
  },
  methods: {
    getDebtor(){
      this.$backend.$fetchDebtor(this.$route.params.id)
      .then(response => {
        this.debtorId = response.id
        this.firstName = response.first_name
        this.lastName = response.last_name
        this.email = response.email
        this.iban = response.iban
        console.log(response)
      })
      .catch(error => {
        if(error.response.status==403){
          console.log('unauthorized')
          //this.$router.go('debtors/')
        }
      })
    },
    formValidate(){
      let isValid = true
      this.nameRules.forEach((rules) => { if (rules(this.firstName) !== true) { isValid = false } })
      this.nameRules.forEach((rules) => { if (rules(this.lastName) !== true) { isValid = false } })
      this.emailRules.forEach((rules) => { if (rules(this.email) !== true) { isValid = false } })
      this.ibanRules.forEach((rules) => { if (rules(this.iban) !== true) { isValid = false } })
      this.valid = isValid
    },
    submit(){
      if(this.$refs.form.validate()){
        let new_debtor = {
          first_name: this.firstName,
          last_name: this.lastName,
          email: this.email,
          iban: this.iban,
        }
        this.$backend.$putDebtor(this.debtorId, new_debtor)
        .then(response => {
          console.log(response)
          console.log('done')
        })
      }
    }
  },
  mounted() {
    this.getDebtor()
  },
  
  updated(){
    this.formValidate();
  }
}