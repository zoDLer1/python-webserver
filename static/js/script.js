axios({
    method: 'post',
    url: 'http://localhost:8080/test',
    data: {
      firstName: 'Fred',
      lastName: 'Flintstone'
    }
  }).then(function (response) {
    console.log(response.data)
  });