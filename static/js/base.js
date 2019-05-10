// Will fade out any messages
setTimeout(function() {
    $('#message').fadeOut('slow')
}, 3000);


if (document.querySelector('#search-submit')) {
    document.querySelector('#search-submit').addEventListener('click', store_user_search)
}

// Will Store Values for user Search 
function store_user_search() {
    var search_bar = document.querySelector('#search-bar');

    if (search_bar) {

        var bedrooms = search_bar.querySelector('#bedrooms');
        var price = search_bar.querySelector('#price');

        search_bar_inputs = {
            'keywords': search_bar.querySelector('#keywords').value,
            'location': search_bar.querySelector('#location').value,
            'bedrooms_key': bedrooms.selectedOptions[0].value,
            'bedroom_index': bedrooms.selectedIndex,
            'bedrooms_value': bedrooms.value,
            'price_key': price.selectedOptions[0].value,
            'price_index': price.selectedIndex,
            'price_value': price.value
        };
    };

    localStorage.setItem(
        'search_bar_inputs', JSON.stringify(search_bar_inputs)
    )
}
