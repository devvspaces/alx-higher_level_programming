$(() => {
  $('div#add_item').click(() => {
    const el = '<li>Item</li>';
    $('ul.my_list').append(el);
  });
});
