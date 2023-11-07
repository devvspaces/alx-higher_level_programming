$(() => {
  const url = 'https://swapi.co/api/films/?format=json';

  function isSuccess (status) {
    return status === 'success';
  }

  $.get(url, function (data, status) {
    if (isSuccess(status)) {
      const films = data.results;
      for (const i in films) {
        $('#list_movies').append('<li>' + films[i].title + '</li>');
      }
    }
  });
});
