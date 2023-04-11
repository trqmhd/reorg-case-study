import axios from "axios";


// instance.
const http = axios.create({
  baseURL: process?.env?.NEXT_PUBLIC_BASE_URI,
  headers: {
    'Authorization': `Bearer example`,
    'Content-Type': 'application/json'
  },
})

export {
  http
}