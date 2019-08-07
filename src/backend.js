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

$backend.$fetchMessages = () => {
    return $backend.get(`messages/`)
        .then(response => response.data)
}

$backend.$postMessage = (payload) => {
    return $backend.post(`messages/`, payload)
        .then(response => response.data)
}

$backend.$deleteMessage = (msgId) => {
    return $backend.delete(`messages/${msgId}`)
        .then(response => response.data)
}

$backend.$googleLogin = (token) => {
  return $backend.post('/auth/google/', { access_token: token })
    .then(resp => resp.data.key )
    .catch(err => { console.log(err.response) })
}



export default $backend
