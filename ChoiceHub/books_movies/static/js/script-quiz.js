// Select all cards
const cards = document.querySelectorAll('.card');

// Function to show the active card and hide all others
function showCard(cardId) {
    cards.forEach((card) => {
        if (card.id === cardId) {
            card.classList.add('active'); // Show the active card with transition
            card.classList.remove('hidden'); // Remove hidden class to make sure it transitions in
        } else {
            card.classList.remove('active');
            card.classList.add('hidden'); // Hide the inactive card
        }
    });
}

// Function to move to the next card
function nextCard(cardId) {
    const currentCardIndex = Array.from(cards).findIndex(c => c.id === cardId);
    const nextCard = cards[currentCardIndex + 1];

    if (nextCard) {
        showCard(nextCard.id); // Show the next card with a transition
    } else {
        console.log("No more cards.");
    }
}

// Function to handle option click and move to the next card
function submitAnswerAndNext(cardId) {
    nextCard(cardId); // Move to the next card
}

// Add event listeners to option buttons
cards.forEach((card) => {
    const options = card.querySelectorAll('.option');
    options.forEach((option) => {
        option.addEventListener('click', () => {
            submitAnswerAndNext(card.id); // Move to the next card when an option is clicked
        });
    });
});

// Initialize the first card as active
if (cards.length > 0) {
    showCard(cards[0].id); // Show the first card only
} else {
    console.log('No cards found.');
}
