$(() => {
  $('div#update_header').click(() => {
    const newH = 'New Header!!!';
    $('header').text(newH);
  });
});
