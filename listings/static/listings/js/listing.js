var enquiry_form = document.getElementsByClassName('form')[0];
var main_doc = document.getElementsByClassName('listing')[0];

window.onload = function() {
    enquiry_form_height()
    search_bar_values()
}

window.addEventListener('load', (event) => {
    search_bar_values()
    enquiry_form_height()
});

$(window).on('resize', function() {
    enquiry_form_height()
})

function search_bar_values() {
    // This function will retrieve the serach_bar values inputed in another page through local storage.
    
    var search_bar = document.querySelector('#search-bar');

    if (localStorage.getItem('search_bar_inputs')) {
        search_bar_inputs = JSON.parse(localStorage.getItem('search_bar_inputs'));

        search_bar.querySelector('#keywords').value = search_bar_inputs['keywords'];
        search_bar.querySelector('#location').value = search_bar_inputs['location'];
        search_bar.querySelector('#bedrooms').selectedIndex = search_bar_inputs['bedroom_index'];
        search_bar.querySelector('#price').selectedIndex = search_bar_inputs['price_index'];

        // A hidden input will carry the search values over to the server side
        document.querySelector('#search-values').value = localStorage.getItem('search_bar_inputs')
    } else {
        search_bar_inputs = {
            'keywords': '',
            'location': '',
            'bedrooms_key': '',
            'bedroom_index': '',
            'bedrooms_value': '',
            'price_key': '',
            'price_index': '',
            'price_value': ''
        };
    
        document.querySelector('#search-values').value = JSON.stringify(search_bar_inputs)
    } 
}

function enquiry_form_height() {
    window_height = $(window).height()
    if (window_height > 730) {
        $('.form').css('height', window_height * 0.8);
    } else if (window_height > 420) {
        $('.form').css('height', window_height * 0.7);
    } else {
        $('.form').css('height', window_height * 0.6);
    }
}



// Detect all clicks on the document
document.addEventListener('click', function(event) {
    // If user presses the enquiry button
    if (event.target.id == 'enquiry-btn') {
        enquiry_form.classList.remove('hidden');
        main_doc.classList.add('darken');
    } else if (event.target.closest('#enquiry-form') || event.target.id == 'enquiry-form') {
        return
    } else {
        enquiry_form.classList.add('hidden');
        main_doc.classList.remove('darken');
    }
});

// Map
var geolocation = document.querySelector('#geolocation').value.split(", ");
geolocation[0] = parseFloat(geolocation[0]);
geolocation[1] = parseFloat(geolocation[1]);

var mymap = L.map('mapid').setView(geolocation, 15);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: 'pk.eyJ1Ijoic2FsYWFoMDEiLCJhIjoiY2p2ZWVwdHEyMjFtcTRlcDhld2NmdzVmNiJ9.Yg-FLvnI1iUC6e9VKaFkuQ'
}).addTo(mymap);

var marker = L.marker(geolocation).addTo(mymap);