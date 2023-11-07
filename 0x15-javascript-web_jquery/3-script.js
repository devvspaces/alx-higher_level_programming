$(() => {
  $('#red_header').click(() => {
    const color = 'red';
    $('header').addClass(color);
  });
});
