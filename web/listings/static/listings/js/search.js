$(document).ready(function(){
    cards_height()
    listing_img_height()
});

$(window).on('resize', function() {
    cards_height()
    listing_img_height()
})

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