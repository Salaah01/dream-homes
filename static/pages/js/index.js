$(document).ready(function(){
    top_container_size()
    listing_img_height()
    cards_height()
});

// On window resize change the top-container size in accordance to the size of the searchbox.
$(window).on('resize', top_container_size())

function top_container_size() {
    // Resizes the height of the top container in accordance to the height of the search bar.
    if ($(window).width() > 558) {
        $('#top-container').css('height', $('#search-box').height() + 251)
    } else if ($(window).width() > 320) {
        $('#top-container').css('height', $('#search-box').height() + 206)
    } else {
        $('#top-container').css('height', $('#search-box').height() + 196)
    }
}

function listing_img_height() {
    // The maximum height of the listing image = 300px or the smallest of the other images.
    var img_height = 300
    var listing_images = document.querySelectorAll('.card img')

    for (i=0; i<listing_images.length; i++) {
        if (listing_images[i].height < img_height) {
            img_height = listing_images[i].height
        };
    };

    for (i=0; i<listing_images.length; i++) {
        listing_images[i].style.setProperty('height', img_height + 'px')
    };
}

function cards_height() {
    // Checks which card has the max height and sets all the other cards to the same height.
    var cards = document.querySelectorAll('.card');
    var card_height = cards[1].offsetHeight;

    for (i=3; i<cards.length; i+=2) {
        if (cards[i].offsetHeight > card_height) {
            card_height = cards[i].offsetHeight
        }
    }

    for (i=1; i<cards.length; i+=2) {
        cards[i].style.setProperty('height', card_height + 'px')
    }

}