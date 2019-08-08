export default {
  name: 'DebtorsListComponent',
  data() {
    return {
      snackbarNotAllowed: false,
      headers: [
        { text: 'email', value: 'email' },
        { text: 'open invoices', value: 'open_invoices_count' },
        { text: 'overdue invoices', value: 'overdue_invoices_count' },
        { text: 'paid invoices', value: 'paid_invoices_count' },
        { text: 'manage',  },
        { text: '',  },
      ],
      debtors: {},
    }
  },
  methods: {
    getDebtors(){
      this.$backend.$fetchDebtors().then(response => {
        //console.log(resp)
        this.debtors = response
      })
    },
    deleteDebtor(id){

      this.$backend.$deleteDebtor(id)
      .then(response => {
        let idx = this.debtors.findIndex(i => i.id === id)
        this.debtors.splice(idx, 1)
      })
      .catch(error => {
        if(error.response.status==403){
          console.log('unauthorized')
          this.snackbarNotAllowed = true
        }
      })
    }
  },
  mounted() {
    this.getDebtors()
    if(this.$store.getters.isAllowed == false){
      this.snackbarNotAllowed = true
      this.$store.dispatch('clearNotAllowed')
    }
  }
}