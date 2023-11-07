$(() => {
  const url = 'https://swapi.co/api/people/5/?format=json';

  function isSuccess (status) {
    return status === 'success';
  }

  $.get(url, function (data, status) {
    if (isSuccess(status)) {
      $('#character').text(data.name);
    }
  });
});
