import axios from 'axios'

let baseUrl = 'http://127.0.0.1:5000'
//let baseUrl = 'https://preferlucky.com/api'

axios.defaults.withCredentials = true

console.log('145..')
export {axios,baseUrl}