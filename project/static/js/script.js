axios({
    method: 'post',
    url: 'http://localhost/test',
    data: {
      firstName: 'Fred',
      lastName: 'Flintstone'
    }
  }).then(function (response) {
    console.log(response.data)
  });