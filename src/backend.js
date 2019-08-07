import axios from 'axios'

let $backend = axios.create({
  baseURL: '/api',
  timeout: 5000,
  headers: {'Content-Type': 'application/json'}
})

$backend.defaults.xsrfHeaderName = "X-CSRFToken"
$backend.defaults.xsrfCookieName = 'csrftoken'

// Response Interceptor to handle and log errors
$backend.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$backend.$fetchDebtors = () => {
    return $backend.get(`debtors/`)
        .then(response => response.data)
}

$backend.$fetchDebtor = (debtorId) => {
  return $backend.get(`debtors/${debtorId}`)
      .then(response => response.data)
}

$backend.$postDebtor = (payload) => {
    return $backend.post(`debtors/`, payload)
        .then(response => response.data)
}

$backend.$putDebtor = (debtorId, payload) => {
  return $backend.put(`debtors/${debtorId}/`, payload)
      .then(response => response.data)
}

$backend.$deleteDebtor = (debtorId) => {
    return $backend.delete(`debtors/${debtorId}`)
        .then(response => response.data)
}

$backend.$googleLogin = (token) => {
  return $backend.post('/auth/google/', { access_token: token })
    .then(response => response.data.key )
    .catch(err => { console.log(err.response) })
}



export default $backend
