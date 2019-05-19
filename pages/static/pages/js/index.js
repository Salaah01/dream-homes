$(document).ready(function(){
    cards_height()
});

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