import axios from 'axios'

let baseUrl = 'http://192.168.1.2:5000'

axios.defaults.withCredentials = true

console.log('145..')
export {axios,baseUrl}