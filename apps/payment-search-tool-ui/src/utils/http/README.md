# Http utils
http utils based on axios.
* [axios official repo](https://github.com/axios/axios)

# Usages of http utils.

```js
import { dokaneApi } from "@utils/http";

// get request
dokaneApi.get('/example',{
  params: {
    test: 'test'
  }
}).then((response) => {
  // Rest of implementation
}).catch((error) => {
  // Rest of implementation
})

// post request.
dokaneApi.post('/example', {
  test: 'test'
}).then((response) => {
  // Rest of implementation
}).catch((error) => {
  // // Rest of implementation
})
```