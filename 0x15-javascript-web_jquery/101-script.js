$(() => {
  $('div#add_item').click(() => {
    $('ul.my_list').append('<li>Item</li>');
  });
  $('div#remove_item').click(() => {
    const list = $('ul.my_list li');
    if (list.length > 0) {
      list[list.length - 1].remove();
    }
  });
  $('div#clear_list').click(() => {
    $('ul.my_list').empty();
  });
});
