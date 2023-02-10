$.ajax({
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  type: 'GET',
  success: (res) => {
    $('#character').text(res.name);
  }
});
